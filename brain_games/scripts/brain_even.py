#!/usr/bin/env python
from brain_games.cli import welcome_user
from brain_games.task5_code import start_game as even_or_not


def main():
    name = welcome_user()
    print(f'Hello! {name}')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    result = even_or_not()
    if result is True:
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")


if __name__ == '__main__':
    main()
