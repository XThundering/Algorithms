import random
import time


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
