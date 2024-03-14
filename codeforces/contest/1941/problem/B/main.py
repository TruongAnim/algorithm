# https://codeforces.com/contest/1941/problem/B


def main():
    test = int(input())
    for _ in range(test):
        n = int(input())
        a = list(map(int, input().split(' ')))
        is_oke = True
        for i in range(1, n - 1):
            a[i] -= a[i - 1] * 2
            a[i + 1] -= a[i - 1]
            a[i - 1] = 0
            if a[i] < 0:
                is_oke = False
                break
        for i in a:
            if i != 0:
                is_oke = False
        if is_oke:
            print('YES')
        else:
            print('NO')


if __name__ == '__main__':
    main()
