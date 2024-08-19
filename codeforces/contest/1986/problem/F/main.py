# https://codeforces.com/contest/1985/problem/F

def check(v, h, n, A, B, sa):
    _dame = sa
    for i in range(n):
        temp = (v - 1) // B[i]
        _dame += temp * A[i]
    if _dame >= h:
        return True
    return False


def binary_search_integer(low, high, h, n, A, B, sa):
    while low <= high:
        mid = (low + high) // 2
        is_oke = check(mid, h, n, A, B, sa)

        if is_oke:
            high = mid - 1
        else:
            low = mid + 1
    if check(high, h, n, A, B, sa):
        return high
    if check(low, h, n, A, B, sa):
        return low


def main():
    import sys
    sys.stdin = open('input.txt', 'r')
    test = int(input())
    for _ in range(test):
        h, n = map(int, input().split(' '))
        A = list(map(int, input().split(' ')))
        B = list(map(int, input().split(' ')))
        sa = sum(A)
        print(binary_search_integer(1, 4 * (10 ** 10) + 10, h, n, A, B, sa))


if __name__ == '__main__':
    main()
