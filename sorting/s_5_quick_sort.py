import unittest


def quick_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    pivot = arr[n // 2]
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + mid + quick_sort(right)


class TestQuickSort(unittest.TestCase):
    def test_quick_sort(self):
        self.assertEqual(quick_sort([64, 25, 12, 22, 11]), [11, 12, 22, 25, 64])

    def test_empty_array(self):
        self.assertEqual(quick_sort([]), [])

    def test_single_element_array(self):
        self.assertEqual(quick_sort([1]), [1])

    def test_already_sorted_array(self):
        self.assertEqual(quick_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted_array(self):
        self.assertEqual(quick_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_duplicate_elements(self):
        self.assertEqual(quick_sort([4, 5, 5, 4, 3, 3, 2, 1]), [1, 2, 3, 3, 4, 4, 5, 5])


if __name__ == '__main__':
    unittest.main()
