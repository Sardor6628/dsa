import unittest


def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


class TestInsertionSort(unittest.TestCase):
    def test_sorted_array(self):
        self.assertEqual(insertion_sort([64, 25, 12, 22, 11]), [11, 12, 22, 25, 64])

    def test_empty_array(self):
        self.assertEqual(insertion_sort([]), [])

    def test_single_element_array(self):
        self.assertEqual(insertion_sort([1]), [1])

    def test_already_sorted_array(self):
        self.assertEqual(insertion_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted_array(self):
        self.assertEqual(insertion_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_duplicate_elements(self):
        self.assertEqual(insertion_sort([4, 5, 5, 4, 3, 3, 2, 1]), [1, 2, 3, 3, 4, 4, 5, 5])


if __name__ == "__main__":
    unittest.main()
