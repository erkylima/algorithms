import unittest

import numpy as np

from helpers.check_sorted import check_sorted
from helpers.run_algorithm import run_algorithm
from sorting_algorithms.bubble_sort import bubble_sort
from sorting_algorithms.insertion_sort import insertion_sort
from sorting_algorithms.merge_sort import merge_sort
from sorting_algorithms.selection_sort import selection_sort


class RunAlgorithmTestCase(unittest.TestCase):
    def test_merge_sort(self):
        sortable = list(np.random.rand(500))
        merge_sort(sortable)
        self.assertEqual(True, check_sorted(sortable))

    def test_insertion_sort(self):
        sortable = list(np.random.rand(500))
        insertion_sort(sortable)
        self.assertEqual(True, check_sorted(sortable))

    def test_bubble_sort(self):
        sortable = list(np.random.rand(500))
        bubble_sort(sortable)
        self.assertEqual(True, check_sorted(sortable))

    def test_selection_sort(self):
        sortable = list(np.random.rand(500))
        selection_sort(sortable)
        self.assertEqual(True, check_sorted(sortable))

    def test_run_algorithm(self):
        sortable = list(np.random.rand(500))
        run_algorithm(bubble_sort, sortable)
        self.assertEqual(True, check_sorted(sortable))


if __name__ == '__main__':
    unittest.main()
