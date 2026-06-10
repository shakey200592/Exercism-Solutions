"""Calculate steps to reach 1 in the Collatz Conjecture.

The Collatz Conjecture states that for any positive integer:
    - If it's even, divide it by 2.
    - If it's odd, multiply it by 3 and add 1.
Repeating these steps will eventually reach 1.

This module provides a function to count the number of steps
required to reach 1 for a given starting number.
"""


def steps(number):
    """Calculate the number of steps to reach 1 in the Collatz Conjecture.

    Args:
        number: A positive integer to process.

    Returns:
        The number of steps to reach 1.

    Raises:
        ValueError: If the number is not a positive integer.
    """
    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    number_of_steps = 0
    while number != 1:
        number = number // 2 if number % 2 == 0 else 3 * number + 1
        number_of_steps += 1

    return number_of_steps
