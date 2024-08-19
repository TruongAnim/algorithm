# https://codeforces.com/contest/1985/problem/E

import math


def find_dimensions(xx, yy, zz, volume):
    dimensions = []
    max_x = int(volume ** (1 / 3)) + 2
    c = 0
    for x in range(1, min(max_x, xx+1)):
        if volume % x == 0:
            max_y = int((volume / x) ** 0.5) + 2
            for y in range(x, min(max_y, yy+1)):
                c+=1
                if (volume // x) % y == 0:
                    z = volume // (x * y)
                    if x * y * z == volume:
                        dimensions.append((x, y, z))
    return [i for i in dimensions if i[2] <= zz]


def main():
    import sys
    sys.stdin = open('input.txt', 'r')
    test = int(input())
    for _ in range(test):
        x, y, z, k = map(int, input().split(' '))
        x, y, z = sorted((x, y, z))
        dimen = find_dimensions(x, y, z, k)
        _max = 0
        for i in dimen:
            _max = max(_max, (x - i[0]+1) * (y - i[1]+1) * (z - i[2]+1))
        print(_max)


if __name__ == '__main__':
    main()
