"""
This module is a test module used to unit test the bounded_set_iter module

I used those sources:
https://stackoverflow.com/questions/8866652/determine-if-2-lists-have-the-same-elements-regardless-of-order
"""

from Q1 import bounded_subsets
import unittest


class TestBoundedSubsets(unittest.TestCase):

    # def __init__(self):
    #     self.s = [1, 2, 3]
    #     self.c = 4

    def test_bounding(self):
        # test whether all subsets are indeed bounded
        for subset in bounded_subsets([1, 2, 3], 4):
            self.assertTrue(sum(subset) <= 4, "Not all subsets of s are bounded by c")

    def test_correctness(self):
        # test whether all the correct subsets are returned
        expected_res = [[], [1], [2], [3], [1, 2], [1, 3]]
        res = []
        for subset in bounded_subsets([1, 2, 3], 4):
            res.append(subset)
        self.assertTrue(sorted(expected_res) == sorted(res), "Wrong subsets returned")

        # |s| = 1
        s_0 = [1]
        c_0 = 1
        expected_res = [[], [1]]
        res = []
        for subset in bounded_subsets(s_0, c_0):
            res.append(subset)
        self.assertTrue(sorted(expected_res) == sorted(res), "Wrong subsets returned")

        # |s| = 0
        s_1 = []
        c_1 = 1
        expected_res = [[]]
        res = []
        for subset in bounded_subsets(s_1, c_1):
            res.append(subset)
        self.assertTrue(sorted(expected_res) == sorted(res), "Wrong subsets returned")

    def test_non_positive(self):
        # test whether the iterator raises an error when encountering non positive aruments
        s_0 = [1, 2, 3, -4, 0]
        c_0 = 1
        self.assertRaises(TypeError, bounded_subsets, s_0, c_0)

        s_1 = [1,2,3]
        c_1 = -1
        self.assertRaises(TypeError, bounded_subsets, s_1, c_1)
        self.assertRaises(TypeError, bounded_subsets, s_0, c_1)

    def test_type(self):
        # type of list elements is not positive int
        self.assertRaises(TypeError, bounded_subsets, ["hello", "hi", "tal", "zich"], 1)
        # type of target sum is not positive int
        self.assertRaises(TypeError, bounded_subsets, [1, 2 , 3], "hello")
        # both are wrong
        self.assertRaises(TypeError, bounded_subsets, ["hello", "hi", "tal", "zich"], "hello")
        # type of arg1 is not a list
        self.assertRaises(TypeError, bounded_subsets, -8, 1)
