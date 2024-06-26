

"""
Linear Search - In this searching algorithm, we check for the element iteratively from one end to the other.


Time Complexity:

Best Case: In the best case, the key might be present at the first index. So the best case complexity is O(1)
Worst Case: In the worst case, the key might be present at the last index i.e., opposite to the end from which the search has started in the list. So the worst-case complexity is O(N) where N is the size of the list.
Average Case: O(N)
Auxiliary Space: O(1) as except for the variable to iterate through the list, no other variable is used. 

"""

import unittest

def linear_search(arr, arr_length, target):
    for index in range(0,arr_length):
        if arr[index]==target:
            return index
    return -1


class TestLinearSearch(unittest.TestCase):
    def test_target_found(self):
        arr = [5, 1, 8, 3, 2]
        self.assertEqual(linear_search(arr, len(arr), 8), 2)

    def test_target_not_found(self):
        arr = [5, 1, 8, 3, 2]
        self.assertEqual(linear_search(arr, len(arr), 9), -1)

    def test_empty_array(self):
        arr = []
        self.assertEqual(linear_search(arr, len(arr), 1), -1)

    def test_multiple_occurrences(self):
        arr = [4, 2, 4, 3, 1]
        self.assertEqual(linear_search(arr, len(arr), 4), 0)

    def test_search_in_single_element_array(self):
        arr = [7]
        self.assertEqual(linear_search(arr, len(arr), 7), 0)
        self.assertEqual(linear_search(arr, len(arr), 2), -1)

if __name__ == '__main__':
    unittest.main()