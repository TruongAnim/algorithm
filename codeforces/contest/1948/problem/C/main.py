# https://codeforces.com/contest/1948/problem/C


def main():
    import sys
    sys.stdin = open('input.txt', 'r')
    test = int(input())
    for _ in range(test):
        n = int(input())
        A = []
        A.append(input())
        A.append(input())
        x = 1
        y = 1
        is_moving = True
        is_oke = False
        while is_moving:
            is_moving = False
            if (y == 2 and x == n) or (y == 1 and x == n) or (y == 2 and x == n - 1) or (
                    y == 2 and x == n - 2 and A[1][n - 1] == '>'):
                is_oke = True
                break
            if y == 1:
                if A[0][x + 1 - 1] == '>':
                    x += 2
                    is_moving = True
                    continue
                if A[1][x - 1] == '>':
                    x += 1
                    y = 2
                    is_moving = True
                    continue
            else:
                if A[1][x + 1 - 1] == '>':
                    x += 2
                    is_moving = True
                    continue
                if A[0][x - 1] == '>':
                    x += 1
                    y = 1
                    is_moving = True
                    continue

        if is_oke:
            print('YES')
        else:
            print('NO')


if __name__ == '__main__':
    main()
