# https://codeforces.com/contest/1999/problem/B


def main():
    # import sys
    # sys.stdin = open('lv10.csv', 'r')
    test = int(input())
    for _ in range(test):
        a, b, c, d = map(int, input().split(' '))
        result = 0
        if (a > c and b >= d) or (a >= c and b > d):
            result += 1
        if (a > d and b >= c) or (a >= d and b > c):
            result += 1
        if (b > c and a >= d) or (b >= c and a > d):
            result += 1
        if (b > d and a >= c) or (b >= d and a > c):
            result += 1
        print(result)


if __name__ == '__main__':
    main()
