"""
Selection sort is a simple and efficient sorting algorithm that works by repeatedly selecting the smallest (or largest) element from the unsorted portion of the list and moving it to the sorted portion of the list.
"""
import unittest

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_inx = i
        for j in range(i + 1, n):
            if arr[min_inx] > arr[j]:
                min_inx = j
        arr[i], arr[min_inx] = arr[min_inx], arr[i]
    return arr


class TestSelectionSort(unittest.TestCase):
    def test_sorted_array(self):
        self.assertEqual(selection_sort([64, 25, 12, 22, 11]), [11, 12, 22, 25, 64])

    def test_empty_array(self):
        self.assertEqual(selection_sort([]), [])

    def test_single_element_array(self):
        self.assertEqual(selection_sort([1]), [1])

    def test_already_sorted_array(self):
        self.assertEqual(selection_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted_array(self):
        self.assertEqual(selection_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_duplicate_elements(self):
        self.assertEqual(selection_sort([4, 5, 5, 4, 3, 3, 2, 1]), [1, 2, 3, 3, 4, 4, 5, 5])

if __name__ == '__main__':
    unittest.main()