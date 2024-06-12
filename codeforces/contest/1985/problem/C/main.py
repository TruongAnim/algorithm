# https://codeforces.com/contest/1985/problem/C

def main():
    import sys
    sys.stdin = open('input.txt', 'r')
    test = int(input())
    for _ in range(test):
        n = int(input())
        A = list(map(int, input().split(' ')))
        _max = 0
        _sum = 0
        count = 0
        for i in A:
            _max = max(i, _max)
            _sum += i
            if _sum - _max == _max:
                count += 1
        print(count)


if __name__ == '__main__':
    main()
