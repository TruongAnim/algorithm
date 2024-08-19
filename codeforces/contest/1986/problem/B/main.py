# https://codeforces.com/contest/1986/problem/B

def valid(x, y, n, m):
    return 0 <= x < n and 0 <= y < m


def check(a, x, y, n, m):
    _x = [1, -1, 0, 0]
    _y = [0, 0, 1, -1]
    _min = 10 ** 10
    for i in range(4):
        new_x = x + _x[i]
        new_y = y + _y[i]
        if valid(new_x, new_y, n, m):
            _min = min(a[x][y] - a[new_x][new_y], _min)
    return _min


def main():
    import sys
    sys.stdin = open('input.txt', 'r')
    test = int(input())
    for _ in range(test):
        n, m = map(int, input().split(' '))
        A = []
        for i in range(n):
            temp = list(map(int, input().split(' ')))
            A.append(temp)
        while True:
            found = False
            for i in range(n):
                for j in range(m):
                    temp = check(A, i, j, n, m)
                    if temp > 0:
                        A[i][j] -= temp
                        found = True
            if not found:
                break
        for i in range(n):
            for j in range(m):
                print(A[i][j], end=' ')
            print()
        # print('-------------')


if __name__ == '__main__':
    main()
