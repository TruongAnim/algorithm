# https://codeforces.com/contest/1843/problem/A

def main():
    tesecase = int(input())
    for _ in range(tesecase):
        n = int(input())
        a = sorted(map(int, input().split(' ')))
        result = 0
        for i in range(n // 2):
            result += a[n - i - 1] - a[i]
        print(result)


if __name__ == '__main__':
    main()
