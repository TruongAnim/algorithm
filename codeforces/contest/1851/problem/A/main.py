# https://codeforces.com/contest/1851/problem/A

def main():
    test = int(input())
    for _ in range(test):
        n, m, k, h = map(int, input().split(' '))
        a = list(map(int, input().split(' ')))
        result = 0
        for i in a:
            result += check(i, m, k, h)
        print(result)


def check(p, m, k, h):
    diff = abs(h - p)
    for i in range(1, m):
        if diff == i * k:
            return 1
    return 0


if __name__ == '__main__':
    main()
