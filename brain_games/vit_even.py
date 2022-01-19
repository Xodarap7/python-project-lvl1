from distutils.util import strtobool
from random import randint

# from prompt_toolkit import prompt
import prompt

MSG_WELCOME = "Welcome to the Brain Games!"
MSG_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
MSG_WRONG_ANSWER= "is wrong answer ;(. Correct answer was 'no'."
ATTEMPS = 3
MIN_NUM = 1
MAX_NUM = 1000


def check_user_answer(answer: str) -> bool:
    """
    Convert a string representation of truth to true (1) or false (0)
    """
    try:
        result = strtobool(answer)
    except ValueError:
        print("Please answer with yes/no or y/n")
        return False

    return result


def print_wrong_answer(name: str, answer: str) -> None:
    """
    Print message if user answer incorrect
    """
    print(f"{answer} {MSG_WRONG_ANSWER}")
    print(f"Let's try again, {name}")


def greet() -> str:
    """
    Еhe prompt line for entering a user name
    :return string of username
    """
    name = prompt('May I have your name? ')
    print(f"Hello {name}")

    return name


def welcome_msg() -> str:
    """
    Print Welcome message and run greet function
    :return:
    """
    print(MSG_WELCOME)
    return greet()


def get_question() -> int:
    """
    The prompt line for the question
    :return:
    """
    num = randint(MIN_NUM, MAX_NUM)
    print(f"Question: {num}")

    return num


def get_answer() -> str:
    """
    The prompt line for the user response
    :return:
    """
    return prompt('Your answer: ')


def check_rules(num: int, user_answer: str, name: str) -> bool:
    """
    If the user entered the wrong answer, end the game and display a message
    """
    is_odd = check_user_answer(user_answer)

    if (num % 2 and is_odd) or not (num % 2 or is_odd):
        print_wrong_answer(name, user_answer)
        return False
    else:
        print("Correct!")
        return True


def start_game() -> None:
    """
    Start game function
    """
    name = welcome_msg()

    for _, i in enumerate(range(ATTEMPS)):
        num = get_question()
        user_answer = get_answer()

        if not check_rules(num, user_answer, name):
            break

        if i == ATTEMPS - 1:
            print(f"Congratulations, {name}!")


def main():
    start_game()


if __name__ == '__main__':
    main()
