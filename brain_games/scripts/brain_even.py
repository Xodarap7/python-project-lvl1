#!/usr/bin/env python
from ..cli import welcome_user
from ..task5_code import even_or_not


def main():
    name = welcome_user()
    print(f'Hello! {name}')
    result = even_or_not()
    if result is True:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
