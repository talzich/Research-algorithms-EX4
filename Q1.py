"""
This module defines a class who's main utility is to produce an iterator.

I found those sources:
https://www.geeksforgeeks.org/subset-sum-problem-dp-25/,
https://www.geeksforgeeks.org/perfect-sum-problem-print-subsets-given-sum/
they were of no help and can be seen in module first_try
"""
from itertools import chain, combinations

class bounded_subsets:

    def __init__(self, s: list, c: int):
        bounded_subsets.__validate(s, c)
        self.s = sorted(s)
        self.c = c

    def __iter__(self):
        subset_iter = chain.from_iterable(combinations(self.s, r) for r in range(len(self.s) + 1))
        for subset in subset_iter:
            if sum(subset) <= self.c:
                yield list(subset)

    @staticmethod
    def __validate(s: list, c: int):
        """
        This method validates the arguments to the function, before constructing the object, raising errors if needed
        :param s: The list we want to validate. Should contain only positive integers
        :param c: The target sum
        """
        if not (isinstance(s, list) and isinstance(c, int)):
            raise TypeError("argument s should be a list and argument c should be an integer")
        if c <= 0:
            raise TypeError("argument c should be a positive integer")
        for element in s:
            if not isinstance(element, int):
                raise TypeError("All list elements should be positive integers")
            if element <= 0:
                raise TypeError("All list elements should be positive integers")
