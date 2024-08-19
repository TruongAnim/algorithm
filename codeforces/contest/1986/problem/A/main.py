# https://codeforces.com/contest/1986/problem/A
import math


def f(x1, x2, x3, a):
    return math.fabs(x1 - a) + math.fabs(x2 - a) + math.fabs(x3 - a)


def main():
    test = int(input())
    for _ in range(test):
        x1, x2, x3 = map(int, input().split(' '))
        _min = 100
        for i in range(20):
            _min = min(f(x1, x2, x3, i), _min)
        print(int(_min))


if __name__ == '__main__':
    main()
