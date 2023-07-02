# https://codeforces.com/problemset/problem/1475/B

def main():
    test = int(input())
    for _ in range(test):
        n = int(input())
        division = n // 2020
        du = n % 2020
        if du <= division:
            print('YES')
        else:
            print('NO')


if __name__ == '__main__':
    main()
