from random import randint

import prompt

from .templates import get_resolution
import sympy

ATTEMPS = 3
MIN_NUM = 1
MAX_NUM = 100


def get_question() -> int:
    """
    The prompt line for the question
    """

    a = randint(MIN_NUM, MAX_NUM)
    print(f"Question: {a}")

    return a


def get_result(question: int) -> bool:
    """
    The function finds the correct result
    :param question: given task
    :return: result
    """
    return sympy.isprime(question)


def str_to_bool(user_value: str) -> bool:
    """
    The function convert the user's input
    into a result format for comparison in
    the function get_resolution
    """
    
    if user_value == "yes":
        return True
    return False


def start_game():
    """
    Start game function
    """

    for i, _ in enumerate(range(ATTEMPS)):
        question = get_question()
        result = get_result(question)
        user_value = prompt.string("Your answer: ")
        user_value = str_to_bool(user_value)
        resolution = get_resolution(result, user_value)

        if not resolution or i == ATTEMPS - 1:
            return resolution


def main():
    start_game()


if __name__ == '__main__':
    main()
