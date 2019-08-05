# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m


def get_pisano_period():
    fib = [0, 1]
    ind = 2
    while True:
        # Calculate next fib num
        next_fib = (fib[ind - 1] + fib[ind - 2]) % m
        # next_fib = fib[ind - 1] + fib[ind - 2]
        # check if found period
        if next_fib == 1 and fib[ind - 1] == 0:
        # started new sequence: remove last entry and return
            fib.pop()
            return fib
        else:
            fib.append(next_fib)
            ind += 1


def get_fibonacci_huge():
    # Find the fib values for Pisano period
    pisano_period = get_pisano_period()

    # Find the location in the sequence
    seq_loc = n % len(pisano_period)

    return pisano_period[seq_loc]


if __name__ == '__main__':
    inn = input()
    n, m = map(int, inn.split())
    print(get_fibonacci_huge())
