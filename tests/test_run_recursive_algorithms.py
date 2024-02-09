import unittest
import numpy as np

from helpers.check_sorted import check_sorted
from helpers.create_unordened_list import create_unordered_list
from helpers.run_recursive_algorithm import run_recursive_algorithm
from sorting_algorithms.quick_sort import quick_sort


class RunRecursiveAlgorithmTestCase(unittest.TestCase):
    def test_quick_sort(self):
        sortable = list(np.random.rand(50))
        sortable = quick_sort(sortable)
        self.assertEqual(True, check_sorted(sortable))  # add assertion here

    def test_run_recursive_algorithm(self):
        sortable = list(np.random.rand(50))
        sortable = run_recursive_algorithm(quick_sort, sortable)

        self.assertEqual(True, check_sorted(sortable))  # add assertion here


if __name__ == '__main__':
    unittest.main()
