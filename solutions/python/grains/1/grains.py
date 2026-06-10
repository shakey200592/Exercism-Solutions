def square(number):
    """
    Calculates the nth value of the grain sequence on a given square
    Args:
        number:

    Returns:
        int: number of grains on a given square

    """

    if number <= 0 or number > 64:
        raise ValueError("square must be between 1 and 64")

    return int(2 ** (number - 1))


def total():
    term = 1
    total = 0

    for square_num in range(1, 65):
        total += square(square_num)
        term += 1

    return total


print(total())
