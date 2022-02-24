import doctest


# Exercise 3
def triple(x):
    """ Returns the number x tripled
    >>> triple(3)
    9
    >>> triple(0)
    0
    >>> triple(-3)
    -9
    """

    return 3 * x


# Exercise 4
def abs_of_diff(x, y):
    """ Returns the absolute value of the difference between x and y
    >>> abs_of_diff(5, 2)
    3
    >>> abs_of_diff(2, 5)
    3
    """
    return abs(x - y)


# Exercise 5
def km_to_miles(x):
    """ Converts given distance in kilometers to the equivalent distance in miles
    using the conversion factor 1.6km = 1mi
    >>> km_to_miles(1.6)
    1.0
    >>> km_to_miles(1)
    0.625
    """
    return x / 1.6


# Exercise 6
def average_of_three_grades(x, y, z):
    """ Returns the average of three grades, each from 0-100
    >>> average_of_three_grades(0,50,100)
    50.0
    >>> average_of_three_grades(50,65, 50)
    55.0
    >>> average_of_three_grades(0,100,104)
    Traceback (most recent call last):
    ...
    ValueError
    >>> average_of_three_grades(-4, 100, 24)
    Traceback (most recent call last):
    ...
    ValueError
    """
    # input validation
    if (x < 0 or x > 100) or (y < 0 or y > 100) or (z < 0 or z > 100):
        raise ValueError

    return (x + y + z) / 3


# Exercise 7
def average_best_three(x, y, z, a):
    """Returns the average of the best three grades of x, y, z, and a
    >>> average_best_three(0,100,70, 100)
    90.0
    """
    if min(x, y, z, a) == x:
        return average_of_three_grades(y, z, a)
    if min(x, y, z, a) == y:
        return average_of_three_grades(x, z, a)
    if min(x, y, z, a) == z:
        return average_of_three_grades(x, y, a)
    if min(x, y, z, a) == a:
        return average_of_three_grades(z, y, z)


# Exercise 8
def weeks_elapsed(day1, day2):
    """ (int, int) -> int
    day1 and day2 are days in the same year. Return the number of full weeks
    that have elapsed between the two days.
    >>> weeks_elapsed(3, 20)
    2
    >>> weeks_elapsed(20, 3)
    2
    >>> weeks_elapsed(8, 5)
    0
    >>> weeks_elapsed(40, 61)
    3
    """
    return abs_of_diff(day1, day2) // 7


# Exercise 10
def square(num):
    """ (number) -> number
    Return the square of num.
    >>> square(3)
    9
    """
    return num * num


doctest.testmod()
