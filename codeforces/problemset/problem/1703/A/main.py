# https://codeforces.com/problemset/problem/1703/A

def main():
    n = int(input())
    for i in range(n):
        s = input().lower()
        print('YES' if s == 'yes' else 'NO')


if __name__ == '__main__':
    main()
