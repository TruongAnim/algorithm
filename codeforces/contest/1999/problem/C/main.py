# https://codeforces.com/contest/1999/problem/C

def main():
    import sys
    sys.stdin = open('input.txt', 'r')
    test = int(input())
    for _ in range(test):
        n, s, m = map(int, input().split(' '))
        result = False
        a = []
        for i in range(n):
            l, r = map(int, input().split(' '))
            if i == 0 and l >= s:
                result = True
            elif i == n - 1 and m - r >= s:
                result = True
            a.append((l, r))
        for i in range(n - 1):
            b1 = a[i]
            b2 = a[i + 1]
            if b2[0] - b1[1] >= s:
                result = True
        print('YES' if result else 'NO')

if __name__ == '__main__':
    main()
