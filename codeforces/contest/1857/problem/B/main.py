# https://codeforces.com/contest/1856/problem/B


def main():
    test = int(input())
    for _ in range(test):
        a = list(int(i) for i in input())[::-1]
        n = len(a)
        _index = 0
        for i in range(n):
            if a[i] >= 5:
                if a[i] == 10:
                    a[i] = 0
                if i == n - 1:
                    a.append(1)
                    n += 1
                    _index = i + 1
                else:
                    a[i + 1] += 1
                    _index = i + 1
        for i in range(n, _index, -1):
            print(a[i - 1], end='')
        print('0' * (_index))


if __name__ == '__main__':
    main()
