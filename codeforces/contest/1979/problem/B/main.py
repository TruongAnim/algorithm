# https://codeforces.com/contest/1980/problem/B

def main():
    import sys
    sys.stdin = open('input.txt', 'r')
    test = int(input())
    A = [2 ** i for i in range(32)]
    for _ in range(test):
        n, f, k = map(int, input().split(' '))
        A = list(map(int, input().split(' ')))
        T = [(A[i], i + 1) for i in range(n)]
        fv = T[f - 1][0]
        B = sorted(T, key=lambda x: (-x[0], x[1]))
        start, end = 0, 0
        for i in range(n):
            if B[i][0] == fv:
                start = i
                break
        for i in range(n):
            if B[i][0] == fv:
                end = i
        if k <= start:
            print('NO')
        elif k > end:
            print('YES')
        else:
            print('MAYBE')


if __name__ == '__main__':
    main()
