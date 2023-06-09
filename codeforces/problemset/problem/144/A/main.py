# https://codeforces.com/problemset/problem/144/A

def main():
    n = int(input())
    a = list(map(int, input().split(' ')))
    sum = 0
    _min = min(a)
    imin = a[::-1].index(_min)
    imin = len(a) - imin - 1

    for i in range(imin, len(a) - 1):
        a[i], a[i + 1] = a[i + 1], a[i]
        sum += 1

    _max = max(a)
    imax = a.index(_max)

    for i in range(imax, 0, - 1):
        a[i], a[i - 1] = a[i - 1], a[i]
        sum += 1
    print(sum)


if __name__ == '__main__':
    main()
