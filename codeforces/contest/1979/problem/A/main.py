# https://codeforces.com/contest/1979/problem/A

def main():
    test = int(input())
    for _ in range(test):
        n = input()
        A = list(map(int, input().split(' ')))
        _min = 10 ** 10
        for i in range(len(A) - 1):
            _min = min(_min, max(A[i], A[i + 1]))
        print(_min - 1)


if __name__ == '__main__':
    main()