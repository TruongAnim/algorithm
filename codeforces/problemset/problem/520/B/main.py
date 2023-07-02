# https://codeforces.com/problemset/problem/520/B

def main():
    n, m = map(int, input().split(' '))
    print(recursion(n, m))


def recursion(n, m):
    if n == m:
        return 0
    elif n > m:
        return n - m
    else:
        if m % 2 == 0:
            return recursion(n, m // 2) + 1
        else:
            return recursion(n, m // 2 + 1) + 2


if __name__ == '__main__':
    main()
