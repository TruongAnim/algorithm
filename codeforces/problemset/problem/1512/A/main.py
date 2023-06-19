# https://codeforces.com/problemset/problem/1512/A
from collections import Counter


def main():
    testcase = int(input())
    for _ in range(testcase):
        n = int(input())
        a = list(map(int, input().split(' ')))
        _map = Counter(a)
        key_of_largest_value = min(_map, key=_map.get)
        print(a.index(key_of_largest_value) + 1)


if __name__ == '__main__':
    main()
