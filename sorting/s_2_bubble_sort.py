import unittest

"""
Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in the wrong order. This algorithm is not suitable for large data sets as its average and worst-case time complexity is quite high.
"""


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


class TestBubbleSort(unittest.TestCase):
    def test_sorted_array(self):
        self.assertEqual(bubble_sort([64, 25, 12, 22, 11]), [11, 12, 22, 25, 64])

    def test_empty_array(self):
        self.assertEqual(bubble_sort([]), [])

    def test_single_element_array(self):
        self.assertEqual(bubble_sort([1]), [1])

    def test_already_sorted_array(self):
        self.assertEqual(bubble_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted_array(self):
        self.assertEqual(bubble_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_duplicate_elements(self):
        self.assertEqual(bubble_sort([4, 5, 5, 4, 3, 3, 2, 1]), [1, 2, 3, 3, 4, 4, 5, 5])


if __name__ == "__main__":
    unittest.main()
