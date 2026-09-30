import random
from words import WORDS
from feedback import evaluate

MAX_GUESSES = 6
QUIT_COMMANDS = ("q", "quit")


class WordleGame:
    def __init__(self, length=5):
        self.length = length
        self.target = random.choice([w for w in WORDS if len(w) == length])
        self.history = []

    def _is_valid(self, guess):
        return len(guess) == self.length and guess.isalpha()

    def _read_guess(self):
        """Keep asking until the guess is valid. Return None if the player quits."""
        while True:
            guess = input("> ").strip().lower()
            if guess in QUIT_COMMANDS:
                return None
            if self._is_valid(guess):
                return guess
            print(f"Invalid guess. Enter a {self.length}-letter word using letters only.")

    def _print_history(self):
        """Print all accepted guesses, numbered, with their feedback."""
        print("Guess history:")
        for number, (guess, feedback) in enumerate(self.history, start=1):
            print(f"  {number}. {guess.upper()}  {' '.join(feedback)}")

    def _print_summary(self, result):
        """Print the end-of-session summary."""
        print("\n=== Session summary ===")
        print(f"Target word : {self.target.upper()}")
        print(f"Result      : {result}")
        print(f"Guesses used: {len(self.history)}")
        if self.history:
            self._print_history()
        else:
            print("No guesses were made.")

    def run(self):
        print(f"Wordle - {self.length} letters, {MAX_GUESSES} guesses.")
        result = "Lost"
        while len(self.history) < MAX_GUESSES:
            guess = self._read_guess()
            if guess is None:
                print("You quit. The word was:", self.target)
                result = "Quit"
                break

            feedback = evaluate(self.target, guess)
            self.history.append((guess, feedback))
            self._print_history()

            if guess == self.target:
                print(f"You solved it in {len(self.history)} guesses!")
                result = "Won"
                break

            print(f"Guesses left: {MAX_GUESSES - len(self.history)}")
        else:
            print("You lost! The word was:", self.target)

        self._print_summary(result)