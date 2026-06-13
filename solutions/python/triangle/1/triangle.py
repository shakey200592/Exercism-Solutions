def is_triangle(sides):
    # Check triangle inequality
    if (
        (sides[0] + sides[1] >= sides[2])
        and (sides[1] + sides[2] >= sides[0])
        and (sides[0] + sides[2] >= sides[1])
    ):
        return True
    else:
        return False


def equilateral(sides):
    return is_triangle(sides) and len(set(sides)) == 1 and not sides == [0, 0, 0]


def isosceles(sides):
    return (is_triangle(sides) and equilateral(sides)) or (
        is_triangle(sides) and len(set(sides)) == 2 and not sides == [0, 0, 0]
    )


def scalene(sides):
    return is_triangle(sides) and len(set(sides)) == 3 and not sides == [0, 0, 0]
