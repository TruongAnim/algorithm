# https://codeforces.com/problemset/problem/617/A

def main():
    n = int(input())
    temp = n // 5
    if n % 5 == 0:
        print(temp)
    else:
        print(temp + 1)


if __name__ == '__main__':
    main()
