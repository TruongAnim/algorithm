# https://codeforces.com/contest/1899/problem/D


def combination(n):
    if n == 1:
        return 0
    return int(n * (n - 1) / 2)


def count_duplicate(a, n):
    s = sorted(a)
    temp = s[0]
    count = 0
    c1 = 0
    c2 = 0
    result = 0
    for i in s:
        if i == temp:
            count += 1
        else:
            result += combination(count)
            if temp == 1:
                c1 = count
            if temp == 2:
                c2 = count
            count = 1
            temp = i
    result += combination(count)
    if temp == 1:
        c1 = count
    if temp == 2:
        c2 = count
    result += c1 * c2
    print(result)


def main():
    import sys
    sys.stdin = open('input.txt', 'r')
    test = int(input())
    for t in range(test):
        n = int(input())
        a = list(map(int, input().split(' ')))
        count_duplicate(a, n)


if __name__ == '__main__':
    main()
