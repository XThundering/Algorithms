import SortTestHelper


# 简单的选择排序
def selection_sort(arr, n):
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


n = 10000
arr1 = SortTestHelper.generate_random_list(n, 0, n)
SortTestHelper.test_sort('Selection Sort', selection_sort, arr1, n)

n = 20000
arr2 = SortTestHelper.generate_random_list(n, 0, n)
SortTestHelper.test_sort('Selection Sort', selection_sort, arr2, n)
