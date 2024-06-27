import unittest
"""
Ternary search is a search algorithm that is used to find the position of a target value within a sorted array. It operates on the principle of dividing the array into three parts instead of two, as in binary search. The basic idea is to narrow down the search space by comparing the target value with elements at two points that divide the array into three equal parts.
"""


def ternary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3
        if arr[mid1] == target:
            return mid1
        elif arr[mid2] == target:
            return mid2
        elif arr[mid1] > target:
            right = mid1 - 1
        elif arr[mid1] < target < arr[mid2]:
            left = mid1 + 1
            right = mid2 - 1
        else:
            left = mid2 + 1
    return -1

class TestTernarySearch(unittest.TestCase):
    def test_target_found_small_array(self):
        arr = [1, 3, 5, 7, 9]
        self.assertEqual(ternary_search(arr, 5), 2)

    def test_target_found_mid_array(self):
        arr = [1, 3, 5, 7, 9, 11, 15, 16, 178, 1998]
        self.assertEqual(ternary_search(arr, 5), 2)

    def test_target_found_large_array(self):
        arr = list(range(100))  # Array of numbers 0-99
        self.assertEqual(ternary_search(arr, 88), 88)

    def test_target_not_found(self):
        arr = [2, 4, 6, 8, 10]
        self.assertEqual(ternary_search(arr, 5), -1)

    def test_empty_array(self):
        arr = []
        self.assertEqual(ternary_search(arr, 1), -1)

    def test_single_element_array_found(self):
        arr = [7]
        self.assertEqual(ternary_search(arr, 7), 0)

    def test_single_element_array_not_found(self):
        arr = [10]
        self.assertEqual(ternary_search(arr, 7), -1)

    def test_large_array_with_duplicates(self):
        arr = [1] * 50 + [2] * 50  # 50 ones followed by 50 twos
        self.assertTrue(ternary_search(arr, 2) in range(50, 100))

    def test_high_values(self):
        arr = [100, 200, 300, 400, 500]
        self.assertEqual(ternary_search(arr, 500), 4)

    def test_low_values(self):
        arr = [100, 200, 300, 400, 500]
        self.assertEqual(ternary_search(arr, 100), 0)

    def test_mixed_types(self):
        arr = ["apple", "banana", "cherry", "date"]
        self.assertEqual(ternary_search(arr, "date"), 3)
        self.assertEqual(ternary_search(arr, "apple"), 0)


if __name__ == '__main__':
    print("Test starts")
    print('........')
    unittest.main()
