# https://codeforces.com/contest/1849/problem/B
# Time limit exceeded
import bisect


def insert_sorted(lst, value):
    index = bisect.bisect_left(lst, value)
    lst.insert(index, value)


def main():
    test = int(input())
    for _ in range(test):
        n, k = map(int, input().split(' '))
        a = list(map(int, input().split(' ')))
        a = list([a[i] % k + k if a[i] > k else a[i], n - i] for i in range(n))
        a = sorted(a, key=lambda x: (x[0], x[1]))

        while len(a) > 0:
            _max = a[-1]
            a.pop()
            _max[0] = _max[0] - k
            if _max[0] > 0:
                insert_sorted(a, [_max[0], _max[1]])
            else:
                print(n - _max[1] + 1, end=' ')
        print()


if __name__ == '__main__':
    main()
