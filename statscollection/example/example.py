"""
The purpose of this module is to show how you can contribute.
"""

import operator


def operator_over_iterable(arg, iterable, binary_operator=operator.add):
    """
    One sentence describing what the function does.

    A more detailed paragraph explaining what the function does.
    This function applies a binary operator (e.g. addition) on an iterable,
    where the second argument of the binary operator is specified by a number.
    Although you should not abuse it, *italic* text may be used for emphasis,
    and fancier typographical elements---such as the em dash---may be used.

    Parameters
    ----------
    arg : any type
        Any argument which is left-compatible with the binary operator.
    iterable : iterable
        An iterable of arguments right-compatible with the binary operator.
    binary_operator : operator
        A binary operator, such as addition, or something else entirely.

    Yields
    ------
    element
        The result of applying the binary operator over the iterable.

    Examples
    --------
    A simple example showing what the function does.

    >>> sequence = [1, 2, 3]
    >>> list(operator_over_iterable(2, sequence))
    [3, 4, 5]

    A more invovled example showing what the function does.

    >>> list(operator_over_iterable(2, sequence, binary_operator=operator.pow))
    [1, 4, 9]

    See [knuth]_.


    References
    ----------

    .. [knuth] Knuth, Donald E.: *The Art of Computer Programming, Volume 1 (3rd Ed.): Fundamental Algorithms*. Addison Wesley Longman Publishing Co., Inc.

    """
    for item in iterable:
        yield binary_operator(item, arg)


class Sum:
    """
    Class level docs.
    """

    def __init__(self, initial_value=0):
        """
        Init docs.
        """
        self.sum = initial_value

    def fit(self, number):
        """
        Fit a new number.
        """
        self.sum += number

    def evaluate(self):
        """
        Evaluate the sum.
        """
        return self.sum

    def __call__(self):
        return self.evaluate()
