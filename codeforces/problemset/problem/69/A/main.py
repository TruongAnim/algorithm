# https://codeforces.com/problemset/problem/69/A

def main():
    n = int(input())
    xx, yy, zz = 0, 0, 0
    for i in range(n):
        x, y, z = map(int, input().split(' '))
        xx += x
        yy += y
        zz += z
    if xx == 0 and yy == 0 and zz == 0:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()
