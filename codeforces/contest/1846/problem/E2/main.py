# https://codeforces.com/contest/1846/problem/E2
import math


def main():
    f = 10 ** 18
    a = set()
    k = 31623
    for i in range(2, k + 1):
        start = i * i + i + 1
        a.add(start)
        for j in range(3, 60):
            start += i ** j
            if start > f:
                break
            a.add(start)

    test = int(input())
    for _ in range(test):
        n = int(input())
        if n in a or (n > k and (check2(n) or check3(n))):
            print('YES')
        else:
            print('NO')


def check2(n):
    discriminant = 4 * n - 3
    sqrt_discriminant = math.isqrt(discriminant)
    if sqrt_discriminant ** 2 == discriminant:
        if (-1 + sqrt_discriminant) % 2 == 0:
            return True

    return False


def check3(n):
    low = 1
    high = n
    while low <= high:
        mid = (low + high) // 2
        equation_value = mid ** 3 + mid ** 2 + mid + 1
        if equation_value == n:
            return True
        elif equation_value < n:
            low = mid + 1
        else:
            high = mid - 1
    return False


if __name__ == '__main__':
    main()
