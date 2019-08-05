# Uses python3
def calc_fib(n):
    if n <= 1:
        return n
    # if n == 2:
    #     return 1
    #
    # fib_arr = [0, 1, 1]
    # for i in range(3, n+1):
    #     fib_arr.append(fib_arr[i-1] + fib_arr[i-2])
    previous, current = 0, 1
    for _ in range(2, n+1):
        previous, current = current, previous + current
    return current


n = int(input())
print(calc_fib(n))
