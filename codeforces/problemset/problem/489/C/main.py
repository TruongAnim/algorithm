# https://codeforces.com/problemset/problem/489/C
# not resolve
_min, _max = 10 * 100, 0


def main():
    m, s = map(int, input().split(' '))
    for i in range(1, 10):
        new_s = s - i
        recursion(m - 1, new_s, i)
    global _min, _max
    print(_min, _max)


def recursion(m, s, a):
    # print(m, s, a)
    if m == 1 and s < 10:
        new_value = a * 10 + s
        global _min, _max
        _min = min(_min, new_value)
        _max = max(_max, new_value)
        print(a * 10 + s)
    else:
        for i in range(10):
            new_a = a * 10 + i
            new_s = s - i
            if m - 1 > 0 and s >= 0:
                recursion(m - 1, new_s, new_a)


if __name__ == '__main__':
    main()
