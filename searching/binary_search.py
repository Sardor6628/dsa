import unittest

"""
Binary Search is defined as a searching algorithm in a sorted array by repeatedly dividing the search interval in half.
The idea of binary search is to use the information that the array sorted and reduced the time Complexity O(log N)

"""


def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


class TestBinarySearch(unittest.TestCase):
    def test_target_found_small_array(self):
        arr = [1, 3, 5, 7, 9]
        self.assertEqual(binary_search(arr, 5), 2)

    def test_target_found_large_array(self):
        arr = list(range(100))  # Array of numbers 0-99
        self.assertEqual(binary_search(arr, 88), 88)

    def test_target_not_found(self):
        arr = [2, 4, 6, 8, 10]
        self.assertEqual(binary_search(arr, 5), -1)

    def test_empty_array(self):
        arr = []
        self.assertEqual(binary_search(arr, 1), -1)

    def test_single_element_array_found(self):
        arr = [7]
        self.assertEqual(binary_search(arr, 7), 0)

    def test_single_element_array_not_found(self):
        arr = [10]
        self.assertEqual(binary_search(arr, 7), -1)

    def test_large_array_with_duplicates(self):
        arr = [1] * 50 + [2] * 50  # 50 ones followed by 50 twos
        self.assertTrue(binary_search(arr, 2) in range(50, 100))

    def test_high_values(self):
        arr = [100, 200, 300, 400, 500]
        self.assertEqual(binary_search(arr, 500), 4)

    def test_low_values(self):
        arr = [100, 200, 300, 400, 500]
        self.assertEqual(binary_search(arr, 100), 0)

    def test_mixed_types(self):
        arr = ["apple", "banana", "cherry", "date"]
        self.assertEqual(binary_search(arr, "date"), 3)
        self.assertEqual(binary_search(arr, "apple"), 0)


if __name__ == '__main__':
    print("Test starts")
    print('........')
    unittest.main()
