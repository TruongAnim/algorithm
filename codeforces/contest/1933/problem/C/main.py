# https://codeforces.com/contest/1933/problem/C
import math


def is_power_of(a, b):
    # Kiểm tra b có phải là lũy thừa của a hay không
    if a <= 1 or b <= 1:
        return False

    # Tính logarithm để kiểm tra
    n = int(round(math.log(b, a)))

    # Kiểm tra n có là số nguyên và a^n có bằng b hay không
    return a ** n == b


def main():
    # import sys
    # sys.stdin = open('lv10.csv', 'r')
    test = int(input())
    for t in range(test):
        a, b, l = map(int, input().split(' '))
        M = set()
        divisible = set()
        for i in range(20):
            for j in range(20):
                M.add(a ** i * b ** j)
        for i in range(1, int(math.sqrt(l)) + 1):
            if l % i == 0:
                div = l // i
                if div in M:
                    divisible.add(l // div)
                if i in M:
                    divisible.add(l // i)
        print(len(divisible))


if __name__ == '__main__':
    main()
