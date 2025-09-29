

# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a classic Hangman game in Python. Practice string manipulation, loops, conditionals, and random selection by creating a word-guessing game where players try to reveal a hidden word before running out of attempts.

## 📝 Tasks

### 🛠️	Hangman Game Logic

#### Description
Create a Python program that lets a player guess letters to reveal a randomly chosen word. The game should track guesses, display progress, and end with a win or lose message.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list
- Accept letter guesses from the user
- Display current progress (e.g., _ a _ _ m a n)
- Track and display the number of incorrect guesses remaining
- End when the word is guessed or attempts are exhausted
- Show a win or lose message at the end

Example:
```
Word: _ a n g m a n
Guesses left: 3
Guessed letters: a, n, g, m
```

### 🛠️	Replay Feature (Optional)

#### Description
Add an option for the player to play another round after the game ends.

#### Requirements
Completed program should:

- Ask the player if they want to play again after each game
- Restart the game with a new word if the player chooses to replay
