from random import randint, choice

import prompt

MSG_WRONG_ANSWER = "is wrong answer ;(. Correct answer was"
MSG_RIGHT_ANSWER = "Correct!"
ATTEMPS = 3
MIN_NUM = 1
MAX_NUM = 10
ACTIONS = "+-*"


def get_question() -> list:
    """
    The prompt line for the question
    :return:
    """
    a = randint(MIN_NUM, MAX_NUM)
    b = randint(MIN_NUM, MAX_NUM)
    action = "".join(choice(ACTIONS) for i in range(1))
    question = [a, action, b]
    print(f"Question: {a}{action}{b}")

    return question


def get_result(question: list) -> int:
    a, action, b = question
    if action == "+":
        return a + b
    elif action == "-":
        return a - b
    elif action == "*":
        return a * b


def get_user_value() -> int:

    return prompt.integer("Your answer: ")


def get_resolution(result: int, user_value: int) -> bool:

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

        if not resolution:
            return resolution

        if i == ATTEMPS - 1:
            print(f"Congratulations, !")
            return resolution


def main():
    start_game()


if __name__ == '__main__':
    main()
