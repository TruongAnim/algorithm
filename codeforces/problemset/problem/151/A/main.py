# https://codeforces.com/problemset/problem/151/A

def main():
    n, k, l, c, d, p, nl, np = map(int, input().split(' '))
    a1 = k * l // nl
    a2 = c * d
    a3 = p // np
    print(min(a1, a2, a3) // n)


if __name__ == '__main__':
    main()
