# https://codeforces.com/problemset/problem/80/A
import math


def is_prime(n):
    if n <= 1:
        return False

        # Check for divisors from 2 to square root of n
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


def main():
    n, m = map(int, input().split(' '))
    for i in range(n + 1, m + 1):
        result = is_prime(i)
        if result and i == m:
            print('YES')
            return
        if result:
            print('NO')
            return
    print("NO")


if __name__ == '__main__':
    main()
