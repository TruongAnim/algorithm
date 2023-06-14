# https://codeforces.com/problemset/problem/230/B
import math


def main():
    n = int(input())
    a = list(map(int, input().split(' ')))
    primes = prime_filter()
    for i in a:
        s = int(math.sqrt(i))
        if s ** 2 == i and s in primes:
            print('YES')
        else:
            print('NO')


def prime_filter():
    a = [i for i in range(10 ** 6)]
    result = set()
    for i in range(2, len(a)):
        if a[i] != 0:
            result.add(a[i])
            for j in range(a[i], 10 ** 6, a[i]):
                a[j] = 0

    return result


if __name__ == '__main__':
    main()
