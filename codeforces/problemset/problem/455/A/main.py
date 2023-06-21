# https://codeforces.com/problemset/problem/455/A
from collections import Counter


def main():
    n = int(input())
    a = tuple(map(int, input().split(' ')))
    a = dict(Counter(a))
    l = sorted(a.keys())
    m = [i * a[i] for i in l]
    if len(l) == 1:
        print(m[0])
        return
    m[1] = max(m[1], m[0]) if l[1] == l[0] + 1 else m[0] + m[1]
    for i in range(2, len(l)):
        if l[i] == l[i - 1] + 1:
            m[i] = max(m[i - 2] + m[i], m[i - 1])
        else:
            m[i] = m[i] + m[i - 1]
    print(m[-1])


if __name__ == '__main__':
    main()
