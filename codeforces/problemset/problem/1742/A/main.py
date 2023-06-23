# https://codeforces.com/problemset/problem/1742/A

def main():
    n = int(input())
    for i in range(n):
        a = sorted(map(int, input().split(' ')))
        print('YES') if a[0] + a[1] == a[2] else print('NO')


if __name__ == '__main__':
    main()
