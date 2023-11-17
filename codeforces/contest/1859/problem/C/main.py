# https://codeforces.com/contest/1859/problem/C


def reverse_second_half(lst, mid):
    lst[mid:] = lst[mid:][::-1]
    return lst


def main():
    test = int(input())
    for _ in range(test):
        n = int(input())
        if n == 2:
            print(2)
            continue
        a = [i + 1 for i in range(n)]
        aa = [reverse_second_half(a.copy(), i) for i in range(1, n)]
        r = max([calculate(n, i) for i in aa])
        print(r)


def calculate(n, l):
    _max = 0
    _sum = 0
    for i in range(n):
        _sum += (i + 1) * l[i]
        _max = max(_max, (i + 1) * l[i])
    return _sum - _max


if __name__ == '__main__':
    main()
