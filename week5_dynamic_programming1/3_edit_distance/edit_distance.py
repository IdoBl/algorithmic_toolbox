# Uses python3
def edit_distance(a, b):
    table = [[float("inf")] * (len(b) + 1)
             for _ in range(len(a) + 1)]
    for i in range(len(a)+1):
        table[i][0] = i
    for j in range(len(b)+1):
        table[0][j] = j

    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            diff = 0 if a[i-1] == b[j-1] else 1
            table[i][j] = min(table[i-1][j]+1,
                              table[i][j-1]+1,
                              table[i-1][j-1]+diff)
    return table[len(a)][len(b)]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
