from game import WordleGame

SUPPORTED_LENGTHS = (4, 5, 6)


def choose_length():
    """Ask until the player picks a supported word length."""
    while True:
        choice = input("Choose word length (4, 5 or 6): ").strip()
        if choice.isdigit() and int(choice) in SUPPORTED_LENGTHS:
            return int(choice)
        print("Invalid choice. Please enter 4, 5 or 6.")


if __name__ == "__main__":
    WordleGame(choose_length()).run()