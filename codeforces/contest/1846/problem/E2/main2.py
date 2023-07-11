# https://codeforces.com/contest/1846/problem/E2


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
    b = set()
    for i in range(k, 10 ** 6):
        s = i * i + i + 1
        b.add(s)
        s += i ** 3
        b.add(s)

    test = int(input())
    for _ in range(test):
        n = int(input())
        if n in a or n in b or (n > 1000000 and has_positive_integer_solutions(1, 1, -(n - 1))):
            print('YES')
        else:
            print('NO')


def has_positive_integer_solutions(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant >= 0:
        sqrt_discriminant = int(discriminant ** 0.5)
        if sqrt_discriminant ** 2 == discriminant:
            if (-b + sqrt_discriminant) % (2 * a) == 0 and (-b - sqrt_discriminant) % (2 * a) == 0:
                return True
    return False


if __name__ == '__main__':
    main()