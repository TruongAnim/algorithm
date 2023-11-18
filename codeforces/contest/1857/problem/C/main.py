# https://codeforces.com/contest/1857/problem/C


def main():
    test = int(input())
    for _ in range(test):
        n = int(input())
        a = sorted(map(int, input().split(' ')))
        current = -1
        result = []
        for i in range(1, n):
            current += (n - i)
            result.append(a[current])
        result.append(10 ** 9)
        # check(result)
        print(' '.join(map(str, result)))


def check(a):
    n = []
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            n.append(min(a[i], a[j]))
    print(n)


if __name__ == '__main__':
    main()
