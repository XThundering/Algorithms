import random
import time


def generate_nearly_ordered_list(n, swap_times):
    arr = [None] * n
    for i in range(n):
        arr[i] = i

    for i in range(swap_times):
        pos_x = random.randint(0, i)
        pos_y = random.randint(0, i)
        arr[pos_x], arr[pos_y] = arr[pos_y], arr[pos_x]
    return arr


def generate_random_list(n, range_l, range_r):
    assert range_l < range_r
    arr = [None] * n
    for i in range(n):
        arr[i] = random.randint(range_l, range_r)
    return arr


def test_sort(sort_name, sort, arr, n):
    start = time.clock()
    sort(arr, n)
    end = time.clock()
    print(sort_name + ' Running time: %s Seconds' % (end - start))
