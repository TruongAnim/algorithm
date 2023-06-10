# https://codeforces.com/problemset/problem/318/A

def main():
    n, k = map(int, input().split(' '))
    odd = (n + 1) // 2
    if k <= odd:
        print(k * 2 - 1)
    else:
        print(2 * (k - odd))


if __name__ == '__main__':
    main()
