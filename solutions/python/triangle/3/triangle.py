"""
Utilities for determining triangle types and validating triangle side lengths.

This module provides functions to determine whether given side lengths form a triangle
and classify triangles into equilateral, isosceles, or scalene categories based on the
side lengths provided.
"""


def is_triangle(sides):
    """
    Determines if a triangle can be formed with the given side lengths.

    This function checks if the given list of side lengths satisfies the triangle
    inequality theorem, which states that the sum of the lengths of any two sides
    of a triangle must be greater than or equal to the length of the third side.

    Arguments:
        sides (list[float|int]): A list containing the lengths of the three sides of a
            potential triangle.

    Returns:
        bool: True if the given side lengths can form a triangle, False otherwise.
    """

    # Check triangle inequality
    return (
        (sides[0] + sides[1] >= sides[2])
        and (sides[1] + sides[2] >= sides[0])
        and (sides[0] + sides[2] >= sides[1])
    )


def equilateral(sides):
    """
    Determines if a triangle is equilateral.

    An equilateral triangle is a triangle in which all three sides are of equal length.
    This function verifies if the given sides form a valid triangle and checks the
    equality of all sides.

    Args:
        sides (list[float|int]): A list of three numerical values representing the lengths
            of the sides of a potential triangle.

    Returns:
        bool: True if the triangle is equilateral, otherwise False.
    """
    return is_triangle(sides) and len(set(sides)) == 1 and not sides == [0, 0, 0]


def isosceles(sides):
    """
    Determines if a triangle is isosceles based on provided side lengths.

    The function evaluates whether the input side lengths satisfy the conditions
    to form an isosceles triangle. To be valid, the sides must first form a
    triangle as defined by the triangle inequality. Additionally, an isosceles
    triangle has at least two sides of equal length, but must not be equilateral.

    Args:
        sides (list[float|int]): A list of three integers representing the lengths
            of the sides of a triangle.

    Returns:
        bool: True if the side lengths form an isosceles triangle, False otherwise.
    """
    return (is_triangle(sides) and equilateral(sides)) or (
        is_triangle(sides) and len(set(sides)) == 2 and not sides == [0, 0, 0]
    )


def scalene(sides):
    """
    Determines if a triangle is scalene.

    A triangle is considered scalene if all three of its sides have different lengths.
    Additionally, the input must represent a valid triangle.

    Args:
        sides (list[float|int]): A list containing the lengths of the three sides of the
            triangle.

    Returns:
        bool: True if the triangle is scalene and valid, False otherwise.
    """
    return is_triangle(sides) and len(set(sides)) == 3 and not sides == [0, 0, 0]
