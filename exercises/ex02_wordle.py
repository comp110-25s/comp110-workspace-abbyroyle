"""Ex2 - Wordle"""

__author__ = "730472123"


def contains_char(search_str: str, single_char: str) -> bool:
    """Checks if letter is found in the string."""
    assert (
        len(single_char) == 1
    ), f"len('{single_char}') is not 1"  # second parameter string length is not 1

    i: int = 0  # index start at 0
    while i < len(search_str):  # iterates over characters in search_str
        if search_str[i] == single_char:
            return True  # seeing if the provided character is found in the word
        i += 1

    return False  # if not, returns false


# defining variables as strings of colored boxed
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(guess: str, secret: str) -> str:
    """Returns an emoji string."""
    assert len(guess) == len(
        secret
    ), "Guess must be same length as secret"  # ensure guess and secret are same lengths

    result: str = ""  # empty string to start
    i: int = 0  # initializes index of 0

    while i < len(guess):  # to iterate over each letter
        if guess[i] == secret[i]:  # correct letter at correct index = green box
            result += GREEN_BOX
        elif contains_char(
            secret, guess[i]
        ):  # correct letter at incorrect index = yellow box
            result += YELLOW_BOX
        else:
            result += WHITE_BOX  # incorrect letter/not in the word
        i += 1

    return result


def input_guess(right_length: int) -> str:
    """Correct length guess."""
    guess: str = input(
        f"Enter a {right_length} character word: "
    )  # asks user for a word of a certain length

    while len(guess) != right_length:
        guess = input(
            f"That wasn't {right_length} chars! Try again: "
        )  # asks until word of correct length is entered

    return guess


def main(secret: str) -> None:
    """Main Wordle loop."""
    turns: int = 1  # starts at first turn
    max_turns: int = 6  # max turns = 6
    won: bool = False  # tracks if player won
    secret_length: int = len(secret)  # find length of secret word

    while (
        turns <= max_turns and not won
    ):  # loops through if <6 turns and player has not won
        print(f"=== Turn {turns}/{max_turns} ===")  # shows turn
        guess: str = input_guess(secret_length)  # asks for guess
        print(emojified(guess, secret))  # shows boxes of gess

        if guess == secret:  # if correct word, player wins and bool is True
            won = True
        else:
            turns += 1  # adds one to number of turns

    if won:
        print(
            f"You won in {turns}/6 turns!"
        )  # prints number of turns it took for player to win
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
