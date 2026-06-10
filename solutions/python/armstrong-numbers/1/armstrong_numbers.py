def is_armstrong_number(number):
    """
    Check if a number is an Armstrong number.

    An Armstrong number is a number that is
    equal to the sum of its digits raised to the power of the number of digits
    in the number. For example, 153 is an Armstrong number because:
    1^3 + 5^3 + 3^3 = 153.

    Args:
        number: int. The input number to check.

    Returns:
        bool. True if the number is an Armstrong number, False otherwise.
    """
    digits = [int(digit) for digit in str(number)]

    sum_square_of_digits = sum(digit ** len(digits) for digit in digits)

    return number == sum_square_of_digits
