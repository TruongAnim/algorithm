# https://codeforces.com/contest/1984/problem/C1
import math


def check_negative(n, A):
    last_neg = -1
    for i in range(n):
        if A[i] < 0:
            last_neg = i
    if last_neg == -1:
        return last_neg
    o1, o2 = A[0], int(math.fabs(A[0]))
    for i in range(1, n):
        t1 = min(o1, o2) + A[i]
        t2 = int(math.fabs(min(o1, o2) + A[i]))
        o1, o2 = t1, t2
    return max(o1, o2)


def check_positive(n, A):
    o1, o2 = A[0], int(math.fabs(A[0]))
    for i in A[1:]:
        t1 = max(o1, o2) + i
        t2 = int(math.fabs(min(o1, o2) + i))
        o1, o2 = t1, t2
    return max(o1, o2)


def check(n, A):
    last_neg = -1
    for i in range(n):
        if A[i] < 0:
            last_neg = i
    if last_neg == -1:
        return sum(A)
    sum_pos, sum_neg, s = 0, 0, 0

    for i in range(last_neg):
        if i > 0:
            sum_pos += A[i]
        if i < 0:
            sum_neg += A[i]
        s += i
    return int(math.fabs(s + A[last_neg])) + sum(A[last_neg:])


def main():
    import sys
    sys.stdin = open('input.txt', 'r')
    test = int(input())
    for _ in range(test):
        n = int(input())
        A = list(map(int, input().split(' ')))
        B = []
        neg, pos = 0, 0
        for i in A:
            if i < 0:
                neg += i
                if pos > 0:
                    B.append(pos)
                    pos = 0
            else:
                pos += i
                if neg < 0:
                    B.append(neg)
                    neg = 0
        if pos > 0:
            B.append(pos)
        if neg < 0:
            B.append(neg)
        if len(B) == 0:
            print(0)
            continue
        p1 = check(len(B), B)
        p2 = check_positive(len(B), B)
        p3 = check_negative(len(B), B)
        print(max(p1, p2, p3))
        # print(p1, p2, p3)


if __name__ == '__main__':
    main()
