import SortTestHelper
from Sorting import merge_sort, merge_sort2


# 对arr[l...r]部分进行partition操作
# 返回p, 使得arr[l...p-1] < arr[p] ; arr[p+1...r] > arr[p]
def __partition(arr, left, right):
    v = arr[left]
    j = left
    for i in range(left+1, right+1):
        if arr[i] < v:
            j += 1
            arr[j], arr[i] = arr[i], arr[j]
    arr[left], arr[j] = arr[j], arr[left]
    return j


# 对arr[l...r]部分进行快速排序
def __quick_sort(arr, left, right):
    if left >= right:
        return

    p = __partition(arr, left, right)
    __quick_sort(arr, left, p-1)
    __quick_sort(arr, p+1, right)


def quick_sort(arr, n):
    __quick_sort(arr, 0, n-1)


n = 100000
arr1 = SortTestHelper.generate_random_list(n, 0, n)
arr2 = arr1[:]
arr3 = arr1[:]
print('n = ' + str(n))
SortTestHelper.test_sort('Merge Sort', merge_sort, arr1, n)
SortTestHelper.test_sort('Merge Sort2', merge_sort2, arr2, n)
SortTestHelper.test_sort('Quick Sort', quick_sort, arr3, n)

n = 200000
arr1 = SortTestHelper.generate_random_list(n, 0, n)
arr2 = arr1[:]
arr3 = arr1[:]
print('n = ' + str(n))
SortTestHelper.test_sort('Merge Sort', merge_sort, arr1, n)
SortTestHelper.test_sort('Merge Sort2', merge_sort2, arr2, n)
SortTestHelper.test_sort('Quick Sort', quick_sort, arr3, n)
