# https://codeforces.com/contest/1976/problem/B

def check(A, B):
    result = 0
    end = B[-1]
    need = 10**10
    for i, j in zip(A, B):
        if i == j:
            if end == i:
                need = 0
        if i < j:
            result += j - i
            if i <= end <= j:
                need = 0
        if i > j:
            result += i - j
            if i >= end >= j:
                need = 0
    if need != 0:
        for i, j in zip(A, B):
            _min = min(i, j)
            _max = max(i, j)
            m1 = m2 = 10**10
            if end <= _min:
                m1 = _min - end
            if end >= _max:
                m2 = end - _max
            need = min(need, min(m1, m2))
    return result + 1 + need


def main():
    import sys
    sys.stdin = open('input.txt', 'r')
    test = int(input())
    for _ in range(test):
        l = int(input())
        a = list(map(int, input().split(' ')))
        b = list(map(int, input().split(' ')))
        print(check(a, b))


if __name__ == '__main__':
    main()
