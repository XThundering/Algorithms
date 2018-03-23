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
a = SortTestHelper.generate_random_list(n, 0, n)
SortTestHelper.test_sort('Selection Sort', selection_sort, a, n)

n = 20000
a = SortTestHelper.generate_random_list(n, 0, n)
SortTestHelper.test_sort('Selection Sort', selection_sort, a, n)
