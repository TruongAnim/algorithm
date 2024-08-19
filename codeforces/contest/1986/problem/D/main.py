# https://codeforces.com/contest/1985/problem/D

def valid(i, j, n, m):
    return 0 <= i < n and 0 <= j < m


def check(A, n, m, i, j):
    if A[i][j] == '#':
        _x = [1, -1, 0, 0]
        _y = [0, 0, 1, -1]
        count = 0
        for t in range(4):
            new_x = _x[t] + i
            new_y = _y[t] + j
            if valid(new_x, new_y, n, m):
                if A[new_x][new_y] == '#':
                    count += 1
        return count
    else:
        return -1


def main():
    import sys
    sys.stdin = open('input.txt', 'r')
    test = int(input())
    for _ in range(test):
        n, m = map(int, input().split(' '))
        A = []
        for i in range(n):
            A.append(input())
        is_oke = False
        one = []
        for i in range(n):
            for j in range(m):
                r = check(A, n, m, i, j)
                if r == 0:
                    print(i + 1, j + 1)
                    is_oke = True
                    break
                elif r == 1:
                    one.append((i, j))

        if not is_oke:
            print(one[1][0] + 1, one[0][1] + 1)


if __name__ == '__main__':
    main()
