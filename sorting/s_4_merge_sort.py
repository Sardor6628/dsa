import unittest

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    result.sort()
    return result


def merge_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    mid = n // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


class TestMergeSort(unittest.TestCase):
    def test_merge_sort(self):
        self.assertEqual(merge_sort([64, 25, 12, 22, 11]), [11, 12, 22, 25, 64])

    def test_empty_array(self):
        self.assertEqual(merge_sort([]), [])

    def test_single_element_array(self):
        self.assertEqual(merge_sort([1]), [1])

    def test_already_sorted_array(self):
        self.assertEqual(merge_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted_array(self):
        self.assertEqual(merge_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_duplicate_elements(self):
        self.assertEqual(merge_sort([4, 5, 5, 4, 3, 3, 2, 1]), [1, 2, 3, 3, 4, 4, 5, 5])


if __name__ == '__main__':
    unittest.main()
