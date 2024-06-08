from numbers import Number


def subtract_one[T: Number](number: T) -> T:
    return number - 1


def subtract_one_better[T: Number](number: T) -> T:
    return number - 2 + 1
