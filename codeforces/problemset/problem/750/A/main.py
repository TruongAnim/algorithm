# https://codeforces.com/problemset/problem/750/A

def main():
    n, k = map(int, input().split(' '))
    total = 4 * 60 - k
    for i in range(1, n + 1):
        if total >= i * 5:
            total -= i * 5
        else:
            print(i - 1)
            return
    print(n)


if __name__ == '__main__':
    main()
