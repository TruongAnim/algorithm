# https://codeforces.com/problemset/problem/581/A

def main():
    a, b = map(int, input().split(' '))
    r1 = min(a, b)
    a -= r1
    b -= r1
    r2 = max(a // 2, b // 2)
    print(r1, r2)


if __name__ == '__main__':
    main()
