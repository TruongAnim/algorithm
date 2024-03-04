# https://codeforces.com/contest/1934/problem/A
import math


def main():
    test = int(input())
    for _ in range(test):
        n = int(input())
        m = sorted(map(int, input().split(' ')))
        a, b, c, d = m[0], m[-2], m[1], m[-1]
        # print(a, b, c, d)
        print(int(math.fabs(a - b) + math.fabs(b - c) + math.fabs(c - d) + math.fabs(d - a)))


if __name__ == '__main__':
    main()
