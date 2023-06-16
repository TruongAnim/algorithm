# https://codeforces.com/problemset/problem/451/A

def main():
    n = min(map(int, input().split()))
    print('Akshat' if n % 2 else 'Malvika')


if __name__ == '__main__':
    main()
