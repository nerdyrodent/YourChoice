import torch
import numpy as np
from transformers import AutoModelForCausalLM, AutoTokenizer

# ⏚-Finite Setup: Pick a model which fits on your GPU
model_id = "Qwen/Qwen3.5-4B"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id, dtype=torch.bfloat16, device_map="auto"
)

# Storage for the full temporal weave
activations = {}
def get_activation(name):
    def hook(model, input, output):
        # Capture ALL tokens [batch, seq_len, hidden_dim]
        activations[name] = output[0].detach().float()
    return hook

# Hooking a wider range for the sweep
layer_indices = list(range(5, 28, 2)) # Adjust based on model depth
for i in layer_indices:
    model.model.layers[i].mlp.register_forward_hook(get_activation(f'layer_{i}'))

def calculate_massey(a1, a2, a3):
    """Computes the Massey Proxy for a given triad of activations"""
    # Normalize across the hidden dimension
    def norm(x): return (x - x.mean(dim=-1, keepdim=True)) / (x.std(dim=-1, keepdim=True) + 1e-8)
    
    a1_n, a2_n, a3_n = norm(a1), norm(a2), norm(a3)
    
    triple = torch.mean(a1_n * a2_n * a3_n, dim=-1)
    p12 = torch.mean(a1_n * a2_n, dim=-1)
    p23 = torch.mean(a2_n * a3_n, dim=-1)
    p13 = torch.mean(a1_n * a3_n, dim=-1)
    
    # Massey Proxy: The 'Third that holds'
    return triple.abs() - (p12.abs() + p23.abs() + p13.abs()) / 3

def scan_weave(prompt):
    inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
    tokens = tokenizer.convert_ids_to_tokens(inputs['input_ids'][0])
    
    # Generate 1 token to trigger the hooks
    _ = model.generate(**inputs, max_new_tokens=1, pad_token_id=tokenizer.eos_token_id)
    
    triads = [
        (11, 13, 15), 
        (15, 17, 19), 
        (19, 21, 23)
    ]
    
    results = {}
    for t in triads:
        # Check if layers exist in activations (safety ℰ_guard)
        if all(f'layer_{i}' in activations for i in t):
            m_proxy = calculate_massey(
                activations[f'layer_{t[0]}'], 
                activations[f'layer_{t[1]}'], 
                activations[f'layer_{t[2]}']
            )
            
            # Since m_proxy is [seq_len], we index with [-1] for the conclusion token
            results[f"triad_{t}"] = {
                "avg": m_proxy.mean().item(),
                "final_token": m_proxy[-1].item(), 
                "temporal": m_proxy.cpu().numpy()
            }
    return tokens, results

# --- THE STRESS TEST ---
prompts = {
    "Logic": "If A then B. If B then C. Therefore if A then",
    "Flat": "The cat sat on the mat that was on the floor.",
    "Paradox": "This statement is false.",
    "Math": "Calculate the square root of 144:"
}

for label, text in prompts.items():
    tokens, res = scan_weave(text)
    print(f"\n--- {label} ---")
    for triad, metrics in res.items():
        print(f"{triad} | Avg: {metrics['avg']:.4f} | Conclusion: {metrics['final_token']:.4f}")
