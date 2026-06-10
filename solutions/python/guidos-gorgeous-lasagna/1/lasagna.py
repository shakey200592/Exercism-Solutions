# Constants
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    Parameters:
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: The remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """
    Calculates the preparation time for the lasagna in minutes

    Parameters
        number_of_layers (int): The number of layers in the lasagna

    Returns:
        int: The preparation time in minutes

    """
    return PREPARATION_TIME * number_of_layers  # Assuming 2 minutes per layer


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculates the elapsed time in minutes.

    Parameters:
        number_of_layers (int): The number of layers in the lasagna.
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: Total time taken in minutes (prep and cooking)

    """

    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
