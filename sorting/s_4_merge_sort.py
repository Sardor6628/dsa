import unittest


# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     end = len(arr) - 1
#     start = 0
#     return mergeSort(arr, start, end)
#
#
# def mergeSort(arr, start, end):
#     if start >= end:
#         return
#     mid = start + (end - start) // 2
#     mergeSort(arr, start, mid)
#     mergeSort(arr, mid + 1, end)
#     merge(arr, start, mid, end)
#     return arr
#
#
# def merge(arr, start, mid, end):
#     leftArrayNum = mid - start + 1
#     rightArrayNum = end - mid
#     leftArray = [0] * leftArrayNum
#     rightArray = [0] * rightArrayNum
#     for i in range(leftArrayNum):
#         leftArray[i] = arr[start + i]
#     for i in range(rightArrayNum):
#         rightArray[i] = arr[mid + 1 + i]
#     indexOfRightArr = 0
#     indexOfLeftArr = 0
#     indexOfMergedArr = start
#
#     while indexOfRightArr < rightArrayNum and indexOfLeftArr < leftArrayNum:
#         if leftArray[indexOfLeftArr] <= rightArray[indexOfRightArr]:
#             arr[indexOfMergedArr] = leftArray[indexOfLeftArr]
#             indexOfLeftArr += 1
#         else:
#             arr[indexOfMergedArr] = rightArray[indexOfRightArr]
#             indexOfRightArr += 1
#         indexOfMergedArr += 1
#     while indexOfLeftArr < leftArrayNum:
#         arr[indexOfMergedArr] = leftArray[indexOfLeftArr]
#         indexOfLeftArr += 1
#         indexOfMergedArr += 1
#     while indexOfRightArr < rightArrayNum:
#         arr[indexOfMergedArr] = rightArray[indexOfRightArr]
#         indexOfMergedArr += 1
#         indexOfRightArr += 1
#     return arr


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort(arr):
    n = len(arr)
    if n <=1:
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
