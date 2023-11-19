# https://codeforces.com/contest/1857/problem/A

def main():
    test = int(input())
    for _ in range(test):
        n = int(input())
        a = list(map(int, input().split(' ')))
        _sum = sum(a)
        if _sum % 2 == 1:
            print('NO')
        else:
            print('YES')


if __name__ == '__main__':
    main()
