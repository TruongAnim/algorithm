# https://codeforces.com/contest/1985/problem/B

def check(a, n):
    s = 0
    for i in range(1, 100):
        if a * i <= n:
            s += a * i
        else:
            break
    return s


def main():
    # import sys
    # sys.stdin = open('input.txt', 'r')
    test = int(input())
    for _ in range(test):
        n = int(input())
        s2 = check(2, n)
        s3 = check(3, n)
        if s2 > s3:
            print(2)
        else:
            print(3)


if __name__ == '__main__':
    main()
