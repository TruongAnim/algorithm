# https://codeforces.com/contest/1847/problem/B

def main():
    test = int(input())
    for _ in range(test):
        n, k = map(int, input().split(' '))
        a = sorted(map(int, input().split(' ')))
        _max = 0
        _current = 0
        for i in range(len(a) - 1):
            if abs(a[i] - a[i + 1]) <= k:
                _current += 1
            else:
                _max = max(_max, _current + 1)
                _current = 0
        _max = max(_max, _current + 1)
        print(n - _max)


def get_char(a):
    for i in a:
        if i != '.':
            return i
    return ''


if __name__ == '__main__':
    main()
