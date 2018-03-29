import sys, random
import SortTestHelper
from Sorting import insertion_sort4, merge_sort2


# 对arr[l...r]部分进行partition操作
# 返回p, 使得arr[l...p-1] < arr[p] ; arr[p+1...r] > arr[p]
def __partition(arr, left, right):

    # 随机在arr[l...r]的范围中, 选择一个数值作为标定点pivot
    arr[left] = arr[random.randint(left, right)]
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
    if right - left <= 15:
        insertion_sort4(arr, left, right)
        return

    p = __partition(arr, left, right)
    __quick_sort(arr, left, p-1)
    __quick_sort(arr, p+1, right)


def quick_sort(arr, n):
    __quick_sort(arr, 0, n-1)


# 测试1 一般测试
n = 100000
arr1 = SortTestHelper.generate_random_list(n, 0, n)
arr2 = arr1[:]
print('Test for random array, size = ' + str(n) + ', random range [0, ' + str(n) + ']')
SortTestHelper.test_sort('Merge Sort2', merge_sort2, arr1, n)
SortTestHelper.test_sort('Quick Sort', quick_sort, arr2, n)
print('')

# 测试2 测试近乎有序的数组
# 加入了随机选择标定点的步骤后, 快速排序可以轻松处理近乎有序的数组
# 但是对于近乎有序的数组, 其效率比优化后的归并排序要低, 但完全再容忍范围里
swap_times = 100
arr1 = SortTestHelper.generate_nearly_ordered_list(n, swap_times)
arr2 = arr1[:]
print('Test for nearly ordered array, size = ' + str(n) + ', swap time = ' + str(swap_times))
SortTestHelper.test_sort('Merge Sort2', merge_sort2, arr1, n)
SortTestHelper.test_sort('Quick Sort', quick_sort, arr2, n)
print('')

# 测试3 测试存在包含大量相同元素的数组
# 但此时, 对于含有大量相同元素的数组, 快速排序算法再次退化成了O(n^2)级别的算法
sys.setrecursionlimit(n)  # 设置Python的最大递归深度为n，因为在包含大量相同元素的数组中，快排递归深度非常大
arr1 = SortTestHelper.generate_random_list(n, 0, 10)
arr2 = arr1[:]
print('Test for random array, size = ' + str(n) + ', random range [0, 10]')
SortTestHelper.test_sort('Merge Sort2', merge_sort2, arr1, n)
SortTestHelper.test_sort('Quick Sort', quick_sort, arr2, n)
