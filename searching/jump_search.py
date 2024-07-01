import unittest
import math


def jump_search(arr, target):
    n = len(arr)
    prev = 0
    step = math.sqrt(n)
    if n == 0:
        return -1
    while arr[int(min(step, n)) - 1] < target:
        prev = step
        step += math.sqrt(n)
        if prev > n:
            return -1
    while arr[int(prev)] < target:
        prev += 1
        if prev == min(step, n):
            return -1
    if arr[int(prev)] == target:
        return int(prev)
    return -1


class TestJumpSearch(unittest.TestCase):
    def test_target_found_small_array(self):
        arr = [1, 3, 5, 7, 9]
        self.assertEqual(jump_search(arr, 5), 2)

    def test_target_found_mid_array(self):
        arr = [1, 3, 5, 7, 9, 11, 15, 16, 178, 1998]
        self.assertEqual(jump_search(arr, 5), 2)

    def test_target_found_large_array(self):
        arr = list(range(100))  # Array of numbers 0-99
        self.assertEqual(jump_search(arr, 88), 88)

    def test_target_not_found(self):
        arr = [2, 4, 6, 8, 10]
        self.assertEqual(jump_search(arr, 5), -1)

    def test_empty_array(self):
        arr = []
        self.assertEqual(jump_search(arr, 1), -1)

    def test_single_element_array_found(self):
        arr = [7]
        self.assertEqual(jump_search(arr, 7), 0)

    def test_single_element_array_not_found(self):
        arr = [10]
        self.assertEqual(jump_search(arr, 7), -1)

    def test_large_array_with_duplicates(self):
        arr = [1] * 50 + [2] * 50  # 50 ones followed by 50 twos
        self.assertTrue(jump_search(arr, 2) in range(50, 100))

    def test_high_values(self):
        arr = [100, 200, 300, 400, 500]
        self.assertEqual(jump_search(arr, 500), 4)

    def test_low_values(self):
        arr = [100, 200, 300, 400, 500]
        self.assertEqual(jump_search(arr, 100), 0)

    def test_mixed_types(self):
        arr = ["apple", "banana", "cherry", "date"]
        self.assertEqual(jump_search(arr, "date"), 3)
        self.assertEqual(jump_search(arr, "apple"), 0)


if __name__ == '__main__':
    # unittest.main()
    unittest.result()
    unittest.removeResult()
