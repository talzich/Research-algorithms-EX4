"""
This module defines a class who's main utility is to produce an iterator.

I used those sources:
https://www.geeksforgeeks.org/subset-sum-problem-dp-25/,
https://www.geeksforgeeks.org/perfect-sum-problem-print-subsets-given-sum/
"""


class bounded_subsets:

    def __init__(self, s: list, c: int):
        bounded_subsets.__validate(s, c)
        self.s = sorted(s)
        self.c = c
        self.subset_size = 0;
        # self.dp_matrix = self.__build_matrix()  # dynamic programming matrix
        # p = []
        # self.__print_subsets(len(s)-1, c, p)

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= len(self.s):
            raise StopIteration
        res = self.s[self.i]
        self.i += 1
        return res

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

    def __build_matrix(self):
        """
        This methods builds a matrix of size len(s)+1 X c+1.
        Each cell in the matrix is a boolean value. A cell [i][j] will hold true if there exists
        a subset of set[0...j-1] with sum less than or equal to i
        :return:
        """

        # starting with all false
        dp_matrix = ([[False for i in range(self.c + 1)] for i in range(len(self.s) + 1)])

        # we can always construct the empty set
        for i in range(len(self.s) + 1):
            dp_matrix[i][0] = True

        for i in range(1, len(self.s) + 1):
            for j in range(1, self.c + 1):
                if j < self.s[i - 1]:
                    dp_matrix[i][j] = dp_matrix[i - 1][j]
                if j >= self.s[i - 1]:
                    dp_matrix[i][j] = (dp_matrix[i - 1][j] or
                                       dp_matrix[i - 1][j - self.s[i - 1]])

        return dp_matrix

    def __print_subsets(self, index: int, c: int, p: list):
        if index == 0 and c != 0 and self.dp_matrix[0][c]:
            p.append(self.s[index])
            if self.s[index] <= c:
                print(p)
            return
        if index == 0 and c == 0:
            print(p)
            return
        if self.dp_matrix[index-1][c]:
            b = p
            self.__print_subsets(index-1, c, b)
        if c >= self.s[index] and self.dp_matrix[index-1][c-self.s[index]]:
            p.append(self.s[index])
            self.__print_subsets(index-1, c-self.s[index], p)

    def __print_matrix(self):
        for i in range(len(self.dp_matrix)):
            for j in range(len(self.dp_matrix[0])):
                print(self.dp_matrix[i][j], end=" ")
            print()


x = bounded_subsets([1, 2, 3], 4)
