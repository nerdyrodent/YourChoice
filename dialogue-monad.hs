{-# LANGUAGE OverloadedStrings #-}

import Text.Read (readMaybe)

-- The core Dialogue monad
data Dialogue s o a
  = Return a
  | Choice s (o -> Dialogue s o a)

instance Functor (Dialogue s o) where
  fmap f (Return a) = Return (f a)
  fmap f (Choice s cont) = Choice s (fmap f . cont)

instance Applicative (Dialogue s o) where
  pure = Return
  Return f <*> d = fmap f d
  Choice s cont <*> d = Choice s (\o -> cont o <*> d)

instance Monad (Dialogue s o) where
  return = Return
  Return a >>= f = f a
  Choice s cont >>= f = Choice s (\o -> cont o >>= f)

-- The interpreter
runDialogue :: (Show s, Read o) => Dialogue s o a -> IO a
runDialogue (Return val) = return val
runDialogue (Choice s cont) = do
  putStrLn $ show s
  input <- getLine
  case readMaybe input of
    Just o  -> runDialogue (cont o)
    Nothing -> do
      putStrLn "Invalid input. Try again."
      runDialogue (Choice s cont)

-- Example dialogue
myFirstDialogue :: Dialogue String Int String
myFirstDialogue = Choice "Choose 1 or 2:" $ \choice ->
  case choice of
    1 -> Return "You chose wisely."
    2 -> Return "You chose... less wisely."
    _ -> Return "That's not even a choice!"

main :: IO ()
main = do
  result <- runDialogue myFirstDialogue
  putStrLn $ "Result: " ++ result
