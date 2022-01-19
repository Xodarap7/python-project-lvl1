from random import randint

import prompt

MIN_NUM = 1
MAX_NUM = 1000


def even_or_not():
    SUCCESS_COUNT = 0
    while SUCCESS_COUNT < 3:

        number = randint(MIN_NUM, MAX_NUM)
        print('Answer "yes" if the number is even, otherwise answer "no".')
        print(f'Question: {number}')
        even_result = 'yes' if number % 2 == 0 else 'no'

        validation = False
        while not validation:
            user_resolution = prompt.string('Your answer: ')
            validation = check_validation(user_resolution)
            if not validation:
                print('You can send "yes" or "no"')
        result = compare_result(user_resolution, even_result)
        if result:
            SUCCESS_COUNT += 1
        else:
            SUCCESS_COUNT = 0
    return True


def check_validation(user_resolution):
    if user_resolution == 'yes' or user_resolution == 'no':
        return True


def compare_result(user_resolution, even_result):
    if even_result == user_resolution:
        print('Correct!')
        return True
    else:
        print(f"'{user_resolution}'"
              f" is wrong answer ;(. Correct answer was '{even_result}'.")
        return False
