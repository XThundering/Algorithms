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


# 插入排序写法2
def insertion_sort2(arr, n):
    for i in range(1, n):
        j = i
        while j > 0 and arr[j] < arr[j-1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1


# 插入排序优化
def insertion_sort3(arr, n):
    for i in range(1, n):
        element = arr[i]

        # j存储element 应该插入的位置
        j = i
        while j > 0 and arr[j-1] > element:
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = element


n = 10000
arr1 = SortTestHelper.generate_random_list(n, 0, n)
arr2 = arr1[:]
arr3 = arr1[:]
arr4 = arr1[:]
print('n = ' + str(n))
SortTestHelper.test_sort('Selection Sort', selection_sort, arr1, n)
SortTestHelper.test_sort('Insertion Sort', insertion_sort, arr2, n)
SortTestHelper.test_sort('Insertion Sort2', insertion_sort2, arr3, n)
SortTestHelper.test_sort('Insertion Sort3', insertion_sort3, arr4, n)

n = 20000
arr1 = SortTestHelper.generate_random_list(n, 0, n)
arr2 = arr1[:]
arr3 = arr1[:]
arr4 = arr1[:]
print('n = ' + str(n))
SortTestHelper.test_sort('Selection Sort', selection_sort, arr1, n)
SortTestHelper.test_sort('Insertion Sort', insertion_sort, arr2, n)
SortTestHelper.test_sort('Insertion Sort2', insertion_sort2, arr3, n)
SortTestHelper.test_sort('Insertion Sort3', insertion_sort3, arr4, n)
