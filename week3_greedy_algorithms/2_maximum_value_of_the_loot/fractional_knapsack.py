# Uses python3
import sys


def get_optimal_value(capacity, weights, values):
    value = 0.
    # Find value to weight ratio for input
    ratio = {weight: value / weight for value, weight in zip(values, weights)}
    # Sort decreasing accord to ratio (i.e., max weight per kg)
    sorted_ratio = [(key, ratio[key]) for key in sorted(ratio, key=ratio.get, reverse=True)]
    # Loop while not used all items
    for i in range(len(sorted_ratio)):
        # If finished fulling the bag
        if capacity == 0:
            return value
        # Take either all weight of biggest item or all weight still in capacity
        a = min(sorted_ratio[i][0], capacity)
        # Add a kilograms of biggest ratio to value
        value += a * sorted_ratio[i][1]
        # Update values
        # sorted_ratio[i][0] -= a
        capacity -= a
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    values = [float(value) for value in values]
    weights = [float(weight) for weight in weights]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
