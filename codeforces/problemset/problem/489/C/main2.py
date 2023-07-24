# https://codeforces.com/problemset/problem/489/C
# not resolve

def main():
    m, s = map(int, input().split(' '))
    _min = -1 if m == 1 and s == 0 else find_min(m, s)
    _max = -1 if _min == -1 else find_max(m, s)

    print(_min, _max)


def find_min(m, s):
    _min = 10 ** m
    for i in range(m + 1):
        j = m - i - 1
        _sum = i * 9 + (j if j > 0 else 0)
        print(i, j, s - _sum)
        if 0 <= s - _sum < 9:
            new_value = int('1' * j + (str(s - _sum) if s - _sum != 0 else '') + '9' * i)
            _min = min(new_value, _min)
            print(_min)
    return _min if _min != 10 ** m else -1


def find_max(m, s):
    if s > m * 9:
        return -1
    _max = 0
    num_9 = s // 9
    mid = s % 9
    zero = m - num_9 - 1
    new_value = int('9' * num_9 + str(mid) + ('0' * zero if zero > 0 else ''))
    _max = max(new_value, _max)
    return _max


if __name__ == '__main__':
    main()
