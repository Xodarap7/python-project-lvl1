from random import randint, choice

import prompt
import math

MSG_WRONG_ANSWER = "is wrong answer ;(. Correct answer was"
MSG_RIGHT_ANSWER = "Correct!"
ATTEMPS = 3
MIN_NUM = 1
MAX_NUM = 100


def get_question() -> list:
    """
    The prompt line for the question
    """

    a = randint(MIN_NUM, MAX_NUM)
    b = randint(MIN_NUM, MAX_NUM)
    question = [a, b]
    print(f"Question: {a} {b}")

    return question


def get_result(question: list) -> int:
    """
    The function finds the correct result
    :param question: given task
    :return: result
    """
    a, b = question
    return math.gcd(a, b)


def get_user_value() -> int:

    return prompt.integer("Your answer: ")


def get_resolution(result: int, user_value: int) -> bool:
    """
    Function checks the result of the user
    :param result: right result
    :param user_value: user input
    :return: resolution
    """
    if result == user_value:
        print(MSG_RIGHT_ANSWER)
        return True

    else:
        print(f"{user_value} {MSG_WRONG_ANSWER} {result},")
        return False


def start_game():
    """
    Start game function
    """

    for i, _ in enumerate(range(ATTEMPS)):
        question = get_question()
        result = get_result(question)
        user_value = get_user_value()
        resolution = get_resolution(result, user_value)

        if not resolution or i == ATTEMPS - 1:
            return resolution


def main():
    start_game()


if __name__ == '__main__':
    main()
