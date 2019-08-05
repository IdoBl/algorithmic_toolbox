# Uses python3
import sys

def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


if __name__ == "__main__":
    inn = input()
    a, b = map(int, inn.split())
    if a >= b:
        print(gcd(a, b))
    else:
        print(gcd(b, a))

