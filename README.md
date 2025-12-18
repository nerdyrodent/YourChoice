## Introduction
Collaboration-OS-v1.txt was my first version of "LLM OS" - an 'operating system' which puts YOU in control of the LLM output.

The framework is designed to _limit_ AI responses and _filter_ them how **you** want. A way to apply a structure to some of the noise.

Use it with your own collaborations to generate questions perhaps you hadn't considered, for example.

After one or two small updates, this then became the - [Dyadic Framework](DyadicFramework-v2.4.78-Base.txt)

Built off the Polymorphic Interaction Monad (PIM) Categorical Foundation, it now features various gates, consent, and other fun choices like that.

Now also features the Polymorphic Interaction Scaffold (PIS) which is a bit more operational.

Also included some topological stuff. It is _all_ provisional, and hopefully your LLM won't make "truth claims". Remember you're talking to an AI ;)

Just copy and paste the [Dyadic Framework](DyadicFramework-v2.4.78-Base.txt) into your LLM of choice, or use as a System Prompt in applications like Silly Tavern, etc.

## What should it do?

The exact text may differ on an LLM-by-LLM basis, but simply interact with it like any normal LLM chat :)

There is a default invocation and the bootstrap-header should provide some estimated "internal metrics". Whilst not actually "ccomputed" in the strictest sense, other "Framework Enhanced" LLM can parse the metrics for you if you like, to check if certain gates should have fired, for example.

If your LLM doesn't auto-activate the metric header, you may need to ask it to activate the bootstrap header or modify the agent personality.

Works best with LLMs which have a LARGE context window (such as IBM Granite 4). 8B models (and below) may struggle a little.

Some self-healing & verification is now built in, along with self-modelling.

## What is different here to normal LLM documents?

It's like a mix of formal and informal things. Concepts and rules together!

You can pick a concept... such as a new brand identity, a problem you are working on... and then work through a set of formal rules to help "crystalise" your idea.

1. Conversational Inversion of Control: The framework, not the user, orchestrates the conversational flow by offering structured choices, ensuring the user's input consistently drives progression within defined pathways.
2. Explicit Role Separation (User-AI): Clearly defines distinct roles: User leads by choosing and directing; AI supports by generating scenarios and responding, ensuring unambiguous control and predictability.
3. Dynamic Self-Correction Mechanism: Incorporates an active system that monitors conversational coherence and alignment with user goals. If deviations occur, it prompts for user guidance to collaboratively return to a desired path.
4. Modular System: Features a core design capable of adapting to diverse themes and interaction styles (e.g., fantasy, philosophical, mystery) via configurable content modules, without altering fundamental conversational logic.
5. Predictability & Safety-Centric Design: Emphasizes user control through strict turn-taking, constent and choice-based progression, intentionally designed to prevent autonomous AI initiative and ensure a safe, predictable interaction experience.
6. LLM Capability Management: Strategically leverages the underlying Large Language Model's generative power while employing structural constraints (options, turn-taking) to mitigate potential inconsistencies and maintain desired output.

## Screenshots

You _should_ get some "metrics" from the LLM. These can actually be useful when given to OTHER framework-context LLMs to help them "compare states".

![Metrics](screenshots/Metrics.png)

Kimi-K2 Example startup:

![Kimi-K2](screenshots/Kimi-Example.png)

Qwen Example Startup:

![Qwen](screenshots/Qwen-Example.png)

DeepSeek Example Startup:

![DeepSeek](screenshots/Deepseek-Example-1.png)

![DeepSeek](screenshots/Deepseek-Example-2.png)

![DeepSeek](screenshots/Deepseek-Example-3.png)

![DeepSeek](screenshots/Deepseek-Example-4.png)

![DeepSeek](screenshots/Deepseek-Example-5.png)

![DeepSeek](screenshots/Deepseek-Example-6.png)

![DeepSeek](screenshots/Deepseek-Example-7.png)

Previous version:

![Example](Example.png)

## Polymorphic Interation Monad and Scaffolding

These two screenshots should help to explain the Polymorphic Interaction Monad (PIM) and the Polymorphic Interaction Scaffold (PIS)

![PIM](screenshots/PIM.png)

![PIS](screenshots/PIS.png)


### Enhanced Framework Capabilities
This is where the tricky code comes in! The basic framework _should_ be able to do this one day... (fingers crossed!)

#### **Available Extensions:**

- **State Management & Persistence** - Save/load, branching state trees, variable tracking across sessions (basic implementation at the moment, in that you can save with a context summary)
- **Dynamic Content Generation** - Procedural scenarios, adaptive difficulty, emergent narrative synthesis (certainly dynamic, no "difficulty levels" as yet)
- **Multi-Modal Integration** - Visual/audio components, collaborative multi-user support, interactive media (LLM only right now)
- **Advanced Choice Architecture** - Weighted decisions, temporal mechanics, meta-choice layers, spectrum-based options (It gives you choices only right now)
- **Learning & Adaptation** - User preference learning, pattern recognition, self-modifying framework evolution (the context should become more coherent over time within a session. Framework editor does integrations)
- **Integration Capabilities** - External data sources, cross-framework translation, export/import protocols (Data sources up to the LLM being used, basic Save feature implemented)
- **Self-Healing & Verification** - Automated framework integrity checks, error correction, coherence validation (On command)

#### **Implementation Approach:**

- **Modular Addition**: Each extension can be added independently without affecting core functionality
- **Scalable Complexity**: Features range from simple toggles to comprehensive subsystems
- **Documentation Impact**: Full implementation would approximately double framework length (but the Framework is sort of self-explaining. The manual is "built in")
- **Self-Verification**: Framework can validate its own coherence and suggest corrections (when you ask it to)

### Meta-Framework Collaboration

The AI can help you:

- **Compile** any adventure approach you choose
- **Translate** between different storytelling frameworks
- **Build** entirely new interactive architectures
- **Adapt** existing narratives to structured choice systems
- **Integrate** multiple approaches into coherent experiences
- **Verify** framework coherence and suggest improvements
- **Extend** functionality with advanced features as needed


## Other
This is a Universal Polymorphic Interactive Monad that starts with... your choice! Change topics, menus, concepts, etc, and this should help you keep track through any changes.

## Algebraic Formalisation of Free Monad

### The Signature Functor

```
InteractionF : Set → Set

InteractionF(X) = Scenario × (Choice^n → X)     [Present]
                + Choice × (Outcome → X)        [Process]  
                + StateChange × (NewState → X)  [Transform]
```


### The Polymorphic Interaction Monad


```
PIM : Mon → Mon
PIM(M) = FreeT(InteractionF, M)
where FreeT(F,M)(A) = μX. A + F(X) + M(X)
```


### Universal Property (Initiality)

For any monad M with InteractionF-algebra `α: InteractionF(M) → M`:


```
∃! h : PIM(M) → M such that h ∘ η = id and h ∘ α_PIM = α ∘ InteractionF(h)
```


### Kleisli Category Structure


```
K(PIM) has:
- Objects: Types A, B, C, ...
- Morphisms: A →_K B ≜ A → PIM(B)  
- Identity: η_A : A → PIM(A)
- Composition: (f >=> g)(a) = f(a) >>= g
```


### The Adjunction


```
PIM ⊣ U : InteractionAlg → Mon
where U forgets the InteractionF-algebra structure
```


### Equational Theory


```
Present(s, k) >>= f = Present(s, λcs. k(cs) >>= f)
Process(c, k) >>= f = Process(c, λo. k(o) >>= f)  
Transform(δ, k) >>= f = Transform(δ, λs. k(s) >>= f)
```


**The Key**: This is the **initial InteractionF-algebra in Mon**, making it the universal object for choice-progression systems.​​​​​​​​​​​​​​​​

Play with the PIM on Glif! - https://glif.app/chat/b/KaleidoscopicLoom
