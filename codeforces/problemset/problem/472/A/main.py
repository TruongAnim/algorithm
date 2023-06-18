# https://codeforces.com/problemset/problem/472/A
import math


def main():
    n = int(input())
    for i in range(2, int(n / 2) + 1):
        if not check_prime(i) and not check_prime(n - i):
            print(i, n - i)
            return


def check_prime(n):
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    main()
