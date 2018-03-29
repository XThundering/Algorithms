import SortTestHelper


def __merge(arr, left, mid, right):
    aux = [None] * (right - left + 1)

    for i in range(left, right + 1):
        aux[i - left] = arr[i]

    i, j = left, mid + 1
    for k in range(left, right + 1):
        if i > mid:
            arr[k] = aux[j - left]
            j += 1
        elif j > right:
            arr[k] = aux[i - left]
            i += 1
        elif aux[i - left] < aux[j - left]:
            arr[k] = aux[i - left]
            i += 1
        else:
            arr[k] = aux[j - left]
            j += 1


def __merge_sort(arr, left, right):
    if left >= right:
        return

    mid = (left + right) // 2
    __merge_sort(arr, left, mid)
    __merge_sort(arr, mid+1, right)
    __merge(arr, left, mid, right)


def merge_sort(arr, n):
    __merge_sort(arr, 0, n-1)


n = 50000
arr = SortTestHelper.generate_random_list(n, 0, n)
print('n = ' + str(n))
SortTestHelper.test_sort('Merge Sort', merge_sort, arr, n)

n = 100000
arr = SortTestHelper.generate_random_list(n, 0, n)
print('n = ' + str(n))
SortTestHelper.test_sort('Merge Sort', merge_sort, arr, n)
