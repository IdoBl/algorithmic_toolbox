# Uses python3
import sys


def find_candidate():
    maj_index = 0
    count = 1
    for i in range(1, len(a)):
        if a[maj_index] == a[i]:
            count += 1
        else:
            count -= 1
        if count == 0:
            maj_index = i
            count += 1

    return a[maj_index]


def find_majority():
    c = find_candidate()
    count = 0
    for i in range(len(a)):
        if a[i] == c:
            count += 1
    return 1 if count > n//2 else 0


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if find_majority():
        print(1)
    else:
        print(0)
