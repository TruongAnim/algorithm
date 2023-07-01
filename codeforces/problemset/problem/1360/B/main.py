# https://codeforces.com/problemset/problem/1360/B

def main():
    test = int(input())
    for _ in range(test):
        n = int(input())
        a = sorted(map(int, input().split(' ')))
        _min = 10 ** 10
        for i in range(n - 1):
            diff = a[i + 1] - a[i]
            _min = min(_min, diff)
        print(_min)


if __name__ == '__main__':
    main()
