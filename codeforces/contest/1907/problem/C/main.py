# https://codeforces.com/contest/1907/problem/C
from collections import Counter


def main():
    # import sys
    # sys.stdin = open('input.txt', 'r')
    test = int(input())
    for t in range(test):
        n = int(input())
        s = input()
        element_count = Counter(s)
        _max = max(element_count.values())
        _sum = sum(element_count.values())
        result = 0 if n % 2 == 0 else 1
        if _max > (_sum - _max):
            temp = _max - (_sum - _max)
            result = max(result, temp)
        print(result)


if __name__ == '__main__':
    main()