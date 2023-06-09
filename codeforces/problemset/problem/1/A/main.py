# https://codeforces.com/problemset/problem/1/A

def main():
    n, m, a = map(int, input().split(' '))
    nn = n // a if n % a == 0 else n // a + 1
    mm = m // a if m % a == 0 else m // a + 1
    print(nn * mm)


if __name__ == '__main__':
    main()
