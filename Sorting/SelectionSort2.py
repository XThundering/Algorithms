import SortTestHelper


# 简单的选择排序
def selection_sort(arr, n):
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


# 选择排序优化 每一轮查找可同时查找未处理元素的最大、最小值
def selection_sort2(arr, n):
    left, right = 0, n-1

    while left < right:
        min_index, max_index = left, right

        # 在每一轮查找时, 要保证arr[minIndex] <= arr[maxIndex]
        if arr[min_index] > arr[max_index]:
            arr[min_index], arr[max_index] = arr[max_index], arr[min_index]

        for i in range(left+1, right):
            if arr[i] < arr[min_index]:
                min_index = i
            elif arr[i] > arr[max_index]:
                max_index = i

        arr[left], arr[min_index] = arr[min_index], arr[left]
        arr[right], arr[max_index] = arr[right], arr[max_index]

        left += 1
        right -= 1


n = 10000
arr1 = SortTestHelper.generate_random_list(n, 0, n)
arr2 = arr1[:]
print('n = ' + str(n))
SortTestHelper.test_sort('Selection Sort', selection_sort, arr1, n)
SortTestHelper.test_sort('Selection Sort2', selection_sort2, arr2, n)

n = 20000
arr1 = SortTestHelper.generate_random_list(n, 0, n)
arr2 = arr1[:]
print('n = ' + str(n))
SortTestHelper.test_sort('Selection Sort', selection_sort, arr1, n)
SortTestHelper.test_sort('Selection Sort2', selection_sort2, arr2, n)
