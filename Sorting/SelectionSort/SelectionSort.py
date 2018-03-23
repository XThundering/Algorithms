# 简单的选择排序
def selection_sort(arr, n):
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


a = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
selection_sort(a, 10)
for num in a:
    print(num, end=' ')
print()
