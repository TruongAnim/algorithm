# https://codeforces.com/contest/2009/problem/C

def main():
    import sys
    sys.stdin = open('input.txt', 'r')
    test = int(input())
    for _ in range(test):
        x, y, k = map(int, input().split(' '))
        h = x // k + (1 if x % k != 0 else 0)
        v = y // k + (1 if y % k != 0 else 0)
        result = max(h, v) * 2
        if h > v and (v - 1) * k <= y:
            result -= 1
        print(result)


if __name__ == '__main__':
    main()
