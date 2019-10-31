# Uses python3
import sys
change_dict = {0: 0}


def get_change(m):
    coins = [1, 3, 4]
    # Base case
    if m == 0:
        return 0
    if m in change_dict:
        return change_dict[m]
    min_num_coins = float('inf')
    for coin in coins:
        if m >= coin:
            num_coins = get_change(m - coin) + 1
        if num_coins < min_num_coins:
            min_num_coins = num_coins
    change_dict[m] = min_num_coins
    return min_num_coins


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
