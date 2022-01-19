from random import randint
import prompt


def even_or_not():
    success_count = 0
    while success_count < 3:

        number = randint(0, 1000)
        print('Answer "yes" if the number is even, otherwise answer "no".')
        print(f'Question: {number}')
        even_result = 'yes' if number % 2 == 0 else 'no'

        validation = False
        while validation is False:
            user_resolution = prompt.string('Your answer: ')
            validation = check_validation(user_resolution)
            if validation is None:
                print('You can send "yes" or "no"')
        result = compare_result(user_resolution, even_result)
        if result is True:
            success_count += 1
        else:
            success_count = 0
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
