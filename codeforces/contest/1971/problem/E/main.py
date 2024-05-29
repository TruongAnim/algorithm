# https://codeforces.com/contest/1971/problem/E
from decimal import Decimal


def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    index = -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            index = mid
            left = mid + 1  # Continue searching to the right for a larger index
        else:
            right = mid - 1

    return index


def main():
    import sys
    sys.stdin = open('input.txt', 'r')
    test = int(input())
    for _ in range(test):
        n, k, q = map(int, input().split(' '))
        A = list(map(int, input().split(' ')))
        B = list(map(int, input().split(' ')))

        for i in range(q):
            t = int(input())
            index = binary_search(A, t)
            if k == 1 or index == -1:
                diff_a = A[0]
                diff_b = B[0]
                diff = t
                v = diff_a / diff_b
                r = int(diff / v)
                print(r, end=' ')
            else:
                if A[index] == t:
                    print(B[index], end=' ')
                else:
                    temp = B[index]
                    diff_a = Decimal(A[index + 1] - A[index])
                    diff_b = Decimal(B[index + 1] - B[index])
                    diff = t - A[index]
                    v = Decimal(diff_a / diff_b)
                    r = int(diff / v)
                    print(temp + r, end=' ')
        print()


if __name__ == '__main__':
    main()
