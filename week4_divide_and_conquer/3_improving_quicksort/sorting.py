# Uses python3
import sys
import random


def partition3(a, l, r):
    # Partitioning using the dutch flag algorithm
    # handle 2 elements array
    if (r - l) <= 1:
        if a[r] < a[l]:
            # Swap elements
            a[l], a[r] = a[r], a[l]
            return l, r
    x = a[l]  # x = lower position value
    i = l
    while i <= r:
        if a[i] < x:
            a[i], a[l] = a[l], a[i]
            l += 1
            i += 1
        elif a[i] > x:
            a[r], a[i] = a[i], a[r]
            r -= 1
        elif a[i] == x:
            i += 1
    return l, r


def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    # use partition3
    m1, m2 = partition3(a, l, r)
    randomized_quick_sort(a, l, m1 - 1)
    randomized_quick_sort(a, m2 + 1, r)
    # #use partition2
    # m = partition2(a, l, r)
    # randomized_quick_sort(a, l, m - 1)
    # randomized_quick_sort(a, m + 1, r)


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
