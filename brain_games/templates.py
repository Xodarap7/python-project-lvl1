import prompt


MSG_WRONG_ANSWER = "is wrong answer ;(. Correct answer was"
MSG_RIGHT_ANSWER = "Correct!"


def get_user_value() -> int:

    return prompt.integer("Your answer: ")


def get_resolution(result, user_value) -> bool:
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
        print(f"'{user_value}' {MSG_WRONG_ANSWER} '{result}'.")
        return False
