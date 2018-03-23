import SortTestHelper


# 简单的选择排序
def selection_sort(arr, n):
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


# 插入排序
def insertion_sort(arr, n):
    for i in range(1, n):
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
            else:
                break


n = 10000
arr1 = SortTestHelper.generate_random_list(n, 0, n)
arr2 = arr1[:]
print('n = ' + str(n))
SortTestHelper.test_sort('Selection Sort', selection_sort, arr1, n)
SortTestHelper.test_sort('Insertion Sort', insertion_sort, arr2, n)

n = 20000
arr1 = SortTestHelper.generate_random_list(n, 0, n)
arr2 = arr1[:]
print('n = ' + str(n))
SortTestHelper.test_sort('Selection Sort', selection_sort, arr1, n)
SortTestHelper.test_sort('Insertion Sort', insertion_sort, arr2, n)
