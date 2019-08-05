# Uses python3


def fib_sum():
    # Calculate Pisano period mod 10 - the sequense is of length 60 according to Lagrange
    pisano_period = [0, 1]
    for ind in range(2, 60):
        # Calculate next fib num
        pisano_period.append((pisano_period[ind - 1] + pisano_period[ind - 2]) % 10)
    # calculate last digit for fib number of f(n+2) % 60- 1
    result = 0
    seq_loc = (n + 2) % 60
    return (pisano_period[seq_loc] - 1) % 10


if __name__ == '__main__':
    inn = input()
    n = int(inn)
    print(fib_sum())
