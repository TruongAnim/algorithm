# https://codeforces.com/contest/1944/problem/B
import random
from collections import Counter


def xor(a):
    result = a[0]
    for i in a[1:]:
        result = result ^ i
    return result


def print_array(a):
    print(' '.join([str(i) for i in a]))


def main():
    import sys
    sys.stdin = open('input.txt', 'r')
    test = int(input())
    for _ in range(test):
        n, k = map(int, input().split(' '))
        A = list(map(int, input().split(' ')))

        CA = Counter(A[:n]).items()
        A1 = sorted([i[0] for i in CA if i[1] == 1])
        A2 = [i[0] for i in CA if i[1] == 2]
        CB = Counter(A[n:]).items()
        B1 = sorted([i[0] for i in CB if i[1] == 1])
        B2 = [i[0] for i in CB if i[1] == 2]
        if len(A1) % 2 != 0:
            A1.pop()
        if len(B1) % 2 != 0:
            B1.pop()
        du = k - len(A1) // 2
        if du > 0:
            for i in range(du):
                A1.append(A2[i])
                A1.append(A2[i])
                B1.append(B2[i])
                B1.append(B2[i])

        print_array(A1[:k * 2])
        print_array(B1[:k * 2])
        # a = xor(A1[:k * 2])
        # b = xor(B1[:k * 2])
        #
        # if a != b:
        #     print(a)
        #     print(b)
        #     print("llllllllllllllll")


if __name__ == '__main__':
    main()
