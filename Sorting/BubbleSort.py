import SortTestHelper
from Sorting import selection_sort, insertion_sort


# 冒泡排序
def bubble_sort(arr, n):
    swapeed = True
    while swapeed:
        swapeed = False
        for i in range(1, n):
            if arr[i-1] > arr[i]:
                arr[i-1], arr[i] = arr[i], arr[i-1]
                swapeed = True

        # 优化：每一趟冒泡循环都将最大的元素放在最后，下一次排序，最后的元素可以不考虑
        n -= 1


# 冒泡循环的优化
def bubble_sort2(arr, n):
    new_n = 1
    while new_n > 0:
        new_n = 0
        for i in range(1, n):
            if arr[i-1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]

                # 记录最后一次交换位置，此处之后的元素下一次扫描不考虑
                new_n = i
        n = new_n


n = 10000
arr1 = SortTestHelper.generate_random_list(n, 0, n)
arr2 = arr1[:]
arr3 = arr1[:]
arr4 = arr1[:]
print('n = ' + str(n))
SortTestHelper.test_sort('Selection Sort', selection_sort, arr1, n)
SortTestHelper.test_sort('Insertion Sort', insertion_sort, arr2, n)
SortTestHelper.test_sort('bubble_sort', bubble_sort, arr3, n)
SortTestHelper.test_sort('bubble_sort2', bubble_sort2, arr4, n)

n = 20000
arr1 = SortTestHelper.generate_random_list(n, 0, n)
arr2 = arr1[:]
arr3 = arr1[:]
arr4 = arr1[:]
print('n = ' + str(n))
SortTestHelper.test_sort('Selection Sort', selection_sort, arr1, n)
SortTestHelper.test_sort('Insertion Sort', insertion_sort, arr2, n)
SortTestHelper.test_sort('bubble_sort', bubble_sort, arr3, n)
SortTestHelper.test_sort('bubble_sort2', bubble_sort2, arr4, n)
