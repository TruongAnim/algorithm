# https://codeforces.com/contest/1850/problem/A

def main():
    test = int(input())
    for _ in range(test):
        a = sorted(map(int, input().split(' ')))
        if a[1] + a[2] >= 10:
            print('YES')
        else:
            print('NO')


if __name__ == '__main__':
    main()
