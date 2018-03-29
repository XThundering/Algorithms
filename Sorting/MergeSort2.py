import SortTestHelper
from Sorting import insertion_sort4, merge_sort


# 将arr[l...mid]和arr[mid+1...r]两部分进行归并
def __merge(arr, left, mid, right):
    aux = [None] * (right - left + 1)

    for i in range(left, right + 1):
        aux[i - left] = arr[i]

    # 初始化，i指向左半部分的起始索引位置l；j指向右半部分起始索引位置mid+1
    i, j = left, mid + 1
    for k in range(left, right + 1):
        if i > mid:  # 如果左半部分元素已经全部处理完毕
            arr[k] = aux[j - left]
            j += 1
        elif j > right:  # 如果右半部分元素已经全部处理完毕
            arr[k] = aux[i - left]
            i += 1
        elif aux[i - left] < aux[j - left]:  # 左半部分所指元素<右半部分所指元素
            arr[k] = aux[i - left]
            i += 1
        else:
            arr[k] = aux[j - left]  # 左半部分所指元素>=右半部分所指元素
            j += 1


def __merge_sort2(arr, left, right):

    # 对于小规模数组，使用插入排序
    if (right - left) <= 15:
        insertion_sort4(arr, left, right)
        return

    mid = (left + right) // 2
    __merge_sort2(arr, left, mid)
    __merge_sort2(arr, mid+1, right)

    if arr[mid] > arr[mid + 1]:
        __merge(arr, left, mid, right)


def merge_sort2(arr, n):
    __merge_sort2(arr, 0, n-1)


n = 100000
arr1 = SortTestHelper.generate_random_list(n, 0, n)
arr2 = arr1[:]
print('n = ' + str(n))
SortTestHelper.test_sort('Merge Sort', merge_sort, arr1, n)
SortTestHelper.test_sort('Merge Sort2', merge_sort2, arr2, n)

n = 200000
arr1 = SortTestHelper.generate_random_list(n, 0, n)
arr2 = arr1[:]
print('n = ' + str(n))
SortTestHelper.test_sort('Merge Sort', merge_sort, arr1, n)
SortTestHelper.test_sort('Merge Sort2', merge_sort2, arr2, n)
