# https://codeforces.com/problemset/problem/490/A

from collections import Counter


def main():
    n = int(input())
    s = {i: [] for i in range(1, 4)}
    a = map(int, input().split(' '))
    for index, i in enumerate(a):
        s[i].append(index+1)
    result = min(len(s[1]), len(s[2]), len(s[3]))
    print(result)
    for i in range(result):
        print(s[1][i], s[2][i], s[3][i])


if __name__ == '__main__':
    main()
