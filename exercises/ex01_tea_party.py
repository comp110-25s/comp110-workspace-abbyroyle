"""This program will allow a user to input a number of guests for a party and calculate the number of teabags and treats for the guests, along with the associated costs."""

__author__: str = "730472123"


def main_planner(guests: int) -> None:
    """Brings the tea party planning functions together and prints the output."""
    print(f"A Cozy Tea Party for {guests} people!")
    print(f"Tea bags: {tea_bags(guests)}")
    print(f"Treats: {treats(guests)}")
    print(f"Cost: ${cost(tea_bags(guests), treats(guests))}")


def tea_bags(people: int) -> int:
    """Calculates the number of tea bags needed."""
    return people * 2


def treats(people: int) -> int:
    """Calculates number of treats based on teas."""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Calculates the cost of tea and treats based on people."""
    return (tea_count * 0.50) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
