#!/usr/bin/env python
from ..task5_code import even_or_not
from ..cli import welcome_user


def main():
    name = welcome_user()
    print(f'Hello! {name}')
    result = even_or_not()
    if result is True:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
