# Uses python3
import sys

def get_change(m):
    if m < 10:
        if m < 5:
            # Can be changed into 1s only
            return m
        else:
            # m >= 5
            return m // 5 + m % 5
    else:
        # m >= 10
        total_coins = 0
        checked_types = [10, 5, 1]
        for checked in checked_types:
            type_coins = m // checked
            total_coins += type_coins
            m -= type_coins * checked
            if m == 0:
                return total_coins


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
