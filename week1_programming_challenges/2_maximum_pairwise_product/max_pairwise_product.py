# python3


def max_pairwise_product(numbers):
    n = len(numbers)

    max_index1 = 0
    for i in range(1, n):
        if numbers[i] > numbers[max_index1]:
            max_index1 = i

    max_index2 = 0 if max_index1 !=0 else 1
    for i in range(n):
        if i != max_index1 and numbers[i] > numbers[max_index2]:
            max_index2 = i

    return numbers[max_index1] * numbers[max_index2]


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
