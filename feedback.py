from collections import Counter


def evaluate(target, guess):
    result = ["gray"] * len(guess)

    # Pass 1: exact matches. Count target letters that were NOT matched exactly.
    remaining = Counter()
    for i, ch in enumerate(guess):
        if ch == target[i]:
            result[i] = "green"
        else:
            remaining[target[i]] += 1

    # Pass 2: yellow only if an unused copy is left in the target.
    for i, ch in enumerate(guess):
        if result[i] == "green":
            continue
        if remaining[ch] > 0:
            result[i] = "yellow"
            remaining[ch] -= 1

    return result