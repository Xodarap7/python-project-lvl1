from random import randint

from .templates import get_resolution, get_user_value

ATTEMPS = 3
MIN_START_NUM = -100
MAX_START_NUM = 100
MIN_STEP = -10
MAX_STEP = 10
PROGRESSION_LEN = 10


def generation_progression() -> list:
    start_num = randint(MIN_START_NUM, MAX_START_NUM)
    progression_step = randint(MIN_STEP, MAX_STEP)
    progression = [start_num]

    while len(progression) < PROGRESSION_LEN:
        progression.append(progression[-1] + progression_step)

    return progression


def get_question() -> int:
    """
    The prompt line for the question
    """
    progression = generation_progression()
    desired_index = randint(0, PROGRESSION_LEN-1)
    print(desired_index)
    result = progression.pop(desired_index)
    progression.insert(desired_index, "..")
    print(f"Question: {progression}")

    return result


def start_game():
    """
    Start game function
    """

    for i, _ in enumerate(range(ATTEMPS)):
        result = get_question()
        user_value = get_user_value()
        resolution = get_resolution(result, user_value)

        if not resolution or i == ATTEMPS - 1:
            return resolution


def main():
    start_game()


if __name__ == '__main__':
    main()
