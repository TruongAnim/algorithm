# https://codeforces.com/contest/1834/problem/B
import math


def main():
    testcase = int(input())
    for _ in range(testcase):
        l, r = input().split(' ')
        l = l.zfill(len(r))
        equal = True
        result = 0
        for i, j in zip(l, r):
            ii = int(i)
            jj = int(j)
            if equal:
                if ii != jj:
                    equal = False
                    result = abs(ii - jj)
            else:
                result += 9
        print(result)


if __name__ == '__main__':
    main()
