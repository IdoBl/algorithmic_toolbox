# Uses python3
import sys

def get_fibonacci_last_digit(n):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(2, n + 1):
        previous, current = current, (previous + current) % 10
        # print("prev: {} , curr: {}".format(previous, current))

    return current


if __name__ == '__main__':
    n = int(input())
    print(get_fibonacci_last_digit(n))
