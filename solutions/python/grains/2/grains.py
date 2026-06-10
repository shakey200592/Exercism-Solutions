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

    # return int(2 ** (number - 1)) # still works but slower than the below

    return 1 << (number - 1) # 1 << (n-1) is the same as 2**n-1 but much faster as it directly operates on bits

    # Examples:
    # 1 << 0 -> 0001 : 0001 = 1
    # 1 << 1 -> 0010 : 0010 = 2
    # 1 << 2 -> 0100 : 0100 = 4
    # 1 << 3 -> 1000 : 1000 = 8





def total():
    term = 1
    total = 0

    for square_num in range(1, 65):
        total += square(square_num)
        term += 1

    return total


print(total())
