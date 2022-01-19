#!/usr/bin/env python
from ..cli import welcome_user
from ..task9_code import start_game as prime

MSG_LOSE_GAME = "Let's try again,"
MSG_WIN_GAME = "Congratulations,"


def main():
    name = welcome_user()
    print(f"Hello! {name}")
    result = prime()

    if not result:
        print(f"{MSG_LOSE_GAME} {name}!")
    else:
        print(f"{MSG_WIN_GAME} {name}!")


if __name__ == "__main__":
    main()
