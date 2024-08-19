# https://codeforces.com/contest/1899/problem/D
# Time limit exceeded

from collections import Counter


def count_elements(arr):
    element_counts = Counter(arr)
    return element_counts


def combination(n):
    if n == 1:
        return 0
    return int(n * (n - 1) / 2)


def count_duplicate(a, n):
    counter = count_elements(a)
    count = sum(map(combination, counter.values()))
    if 2 in counter and 1 in counter:
        count += counter[2] * counter[1]
    print(count)


def get_test_data():
    import random
    return [random.randint(1, 1000) for i in range(100000)]


def main():
    # import sys
    # sys.stdin = open('lv10.csv', 'r')
    test = int(input())
    for t in range(test):
        n = int(input())
        a = list(map(int, input().split(' ')))
        count_duplicate(a, n)


if __name__ == '__main__':
    main()