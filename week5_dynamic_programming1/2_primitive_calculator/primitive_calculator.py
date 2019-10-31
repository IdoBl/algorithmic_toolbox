# Uses python3
import sys
# Memoization cache
cache = {1: [1]}


# Gets recursice error if too deep
def optimal_sequence_recursive(n):
    # If n sequence in cache - return it
    if cache.get(n):
        return cache[n]

    # Not in cache - need to find it
    candidate = optimal_sequence_recursive(n-1) + [n]
    if n % 3 == 0:
        temp_candidate = optimal_sequence_recursive(n // 3) + [n]
        if len(temp_candidate) < len(candidate):
            candidate = temp_candidate
    if n % 2 == 0:
        temp_candidate = optimal_sequence_recursive(n // 2) + [n]
        if len(temp_candidate) < len(candidate):
            candidate = temp_candidate

    # Add to cache
    cache[n] = candidate
    return candidate


def optimal_sequence_iter(n):
    all_parents = [None] * (n + 1)
    all_min_ops = [0] + [None] * n

    for k in range(1, n + 1):
        curr_parent = k - 1
        curr_min_ops = all_min_ops[curr_parent] + 1

        if k % 3 == 0:
            parent = k // 3
            num_ops = all_min_ops[parent] + 1
            if num_ops < curr_min_ops:
                curr_parent, curr_min_ops = parent, num_ops

        if k % 2 == 0:
            parent = k // 2
            num_ops = all_min_ops[parent] + 1
            if num_ops < curr_min_ops:
                curr_parent, curr_min_ops = parent, num_ops

        all_parents[k], all_min_ops[k] = curr_parent, curr_min_ops

    numbers = []
    k = n
    while k > 0:
        numbers.append(k)
        k = all_parents[k]
    numbers.reverse()

    return numbers


input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence_iter(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
