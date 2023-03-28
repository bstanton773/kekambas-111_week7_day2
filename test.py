import unittest
from whiteboard import solution
from unittest import TestCase


class TestDoubleEveryOtherCase(TestCase):

    def test_solution_with_four_elements(self):
        assert solution([1, 2, 3, 4]) == [1, 4, 3, 8]

    def test_solution_with_five_elements(self):
        assert solution([5, 6, 7, 8, 9]) == [5, 12, 7, 16, 9]

    def test_solution_with_three_elements(self):
        assert solution([10, 20, 30]) == [10, 40, 30]

    def test_solution_with_even_elements(self):
        assert solution([2, 4, 6, 8]) == [2, 8, 6, 16]

    def test_solution_with_single_element(self):
        assert solution([1]) == [1]
