#!/usr/bin/env python
from ..cli import welcome_user
from ..task6_code import start_game as calc

MSG_END_GAME = "Let's try again,"
MSG_WIN_GAME = "Congratulations,"


def main():
    name = welcome_user()
    print(f"Hello! {name}")
    result = calc()

    if not result:
        print(f"{MSG_END_GAME} {name}!")
    else:
        print(f"{MSG_WIN_GAME} {name}!")


if __name__ == "__main__":
    main()
