# https://codeforces.com/problemset/problem/313/A

def main():
    n = int(input())
    s = str(n)
    a = int(s[:-1])
    b = int(s[:-2] + s[-1])
    print(max(n, a, b))


if __name__ == '__main__':
    main()
