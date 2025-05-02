# https://codeforces.com/contest/2009/problem/D

def main():
    import sys
    sys.stdin = open('input.txt', 'r')
    test = int(input())
    for _ in range(test):
        n = int(input())
        a, b = [0 for i in range(n + 1)], [0 for i in range(n + 1)]
        ra = []
        rb = []
        for i in range(n):
            x, y = map(int, input().split(' '))
            if y == 0:
                a[x] = 1
                ra.append(x)
            if y == 1:
                b[x] = 1
                rb.append(x)
        result = 0
        for i in range(n):
            if a[i] == b[i] and a[i] == 1:
                result += len(ra) - 1
                result += len(rb) - 1
        for i in range(1, n-1):
            if b[i] == 1 and a[i - 1] == 1 and a[i + 1] == 1:
                result += 1
            if a[i] == 1 and b[i - 1] == 1 and b[i + 1] == 1:
                result += 1
        print(result)


if __name__ == '__main__':
    main()
