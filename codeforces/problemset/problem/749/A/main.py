# https://codeforces.com/problemset/problem/749/A

def main():
    n = int(input())
    print(n // 2)
    if n % 2 == 0:
        print(' '.join(['2'] * (n // 2)))
    else:
        print(' '.join(['2'] * (n // 2 - 1)), 3)


if __name__ == '__main__':
    main()
