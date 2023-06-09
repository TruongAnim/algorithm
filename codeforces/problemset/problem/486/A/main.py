# https://codeforces.com/problemset/problem/486/A

def main():
    n = int(input())
    if n % 2 == 0:
        print(n // 2)
    else:
        print(n // 2 - n)


if __name__ == '__main__':
    main()
