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
