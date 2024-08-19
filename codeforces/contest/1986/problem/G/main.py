# https://codeforces.com/contest/1985/problem/G
def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))


def check(n, k):
    return sum_of_digits(n * k) == k * sum_of_digits(n)


def process(l, r, k):
    count = 0
    for i in range(10 ** l, 10 ** r):
        if check(i, k):
            print('i=', i, k)
            count += 1
    return count


def main():
    import sys
    sys.stdin = open('input.txt', 'r')
    test = int(input())
    num = [0, 10, 5, 4, 3, 2, 2, 2, 2, 2]
    for _ in range(test):
        l, r, k = map(int, input().split(' '))
        if k > 9:
            print(0)
        else:
            # print(process(l, r, k))
            print((num[k] ** r - num[k] ** l) % (10 ** 9 + 7))


if __name__ == '__main__':
    main()
