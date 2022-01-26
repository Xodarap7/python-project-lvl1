from random import randint

import prompt

from brain_games.templates import get_resolution


ATTEMPS = 3
MIN_NUM = 1
MAX_NUM = 100


def get_question() -> int:
    """
    The prompt line for the question
    """
    num = randint(MIN_NUM, MAX_NUM)
    print(f"Question: {num}")

    return num


def get_result(question: int) -> str:
    """
    The function finds the correct result
    :param question: given task
    :return: result
    """
    if question % 2 == 0:
        result = 'yes'
    else:
        result = 'no'
    return result


def start_game():
    """
    Start game function
    """

    for i, _ in enumerate(range(ATTEMPS)):
        question = get_question()
        result = get_result(question)
        user_value = prompt.string("Your answer: ")
        resolution = get_resolution(result, user_value)

        if not resolution or i == ATTEMPS - 1:
            return resolution


def main():
    start_game()


if __name__ == '__main__':
    main()
