# https://codeforces.com/contest/1850/problem/F
# not resolve

from collections import Counter


def main():
    test = int(input())
    for _ in range(test):
        n = int(input())
        a = tuple(i for i in map(int, input().split(' ')) if i <= n)
        a = Counter(a)
        m = {}
        for i in a.keys():
            for j in range(i, n + 1, i):
                if j in m:
                    m[j] += a[i]
                else:
                    m[j] = a[i]
        if len(m.values()) == 0:
            print(0)
        else:
            print(max(m.values()))


if __name__ == '__main__':
    main()
