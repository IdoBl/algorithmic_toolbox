# Uses python3
# import sys

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b


def lcm(bigger, smaller):
    upper_factor = bigger * smaller

    for factor in range(bigger, upper_factor, bigger):
        if factor % smaller == 0:
            return factor

    return upper_factor


if __name__ == '__main__':
    inn = input()
    a, b = map(int, inn.split())
    if a >= b:
        print(lcm(a, b))
    else:
        print(lcm(b, a))
