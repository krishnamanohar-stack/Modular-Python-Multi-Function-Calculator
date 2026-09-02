def validate_number(value):
    try:
        return float(value)
    except ValueError:
        return None

def validate_integer(value):
    number = validate_number(value)

    if number is None:
        return None

    if number != int(number):
        return None

    return int(number)


def validate_positive_integer(value):
    number = validate_integer(value)

    if number is None or number <= 0:
        return None

    return number


def validate_non_negative_integer(value):
    number = validate_integer(value)

    if number is None or number < 0:
        return None

    return number
