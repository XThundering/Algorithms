import SortTestHelper
from Sorting import selection_sort, insertion_sort, bubble_sort


def shell_sort(arr, n):
    h = 1
    while h < n/3:
        h = 3 * h + 1

    while h >= 1:
        for i in range(h, n):
            e = arr[i]
            j = i
            while j >= h and e < arr[j-h]:
                arr[j] = arr[j-h]
                j -= h
            arr[j] = e
        h = h//3


n = 10000
arr1 = SortTestHelper.generate_random_list(n, 0, n)
arr2 = arr1[:]
arr3 = arr1[:]
arr4 = arr1[:]
print('n = ' + str(n))
SortTestHelper.test_sort('Selection Sort', selection_sort, arr1, n)
SortTestHelper.test_sort('Insertion Sort', insertion_sort, arr2, n)
SortTestHelper.test_sort('bubble_sort', bubble_sort, arr3, n)
SortTestHelper.test_sort('shell_sort', shell_sort, arr4, n)

n = 20000
arr1 = SortTestHelper.generate_random_list(n, 0, n)
arr2 = arr1[:]
arr3 = arr1[:]
arr4 = arr1[:]
print('n = ' + str(n))
SortTestHelper.test_sort('Selection Sort', selection_sort, arr1, n)
SortTestHelper.test_sort('Insertion Sort', insertion_sort, arr2, n)
SortTestHelper.test_sort('bubble_sort', bubble_sort, arr3, n)
SortTestHelper.test_sort('shell_sort', shell_sort, arr4, n)
