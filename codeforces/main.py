# https://codeforces.com/problemset/problem/466/A

def main():
    n, m, a, b = map(int, input().split(' '))
    if b / m > a:
        print(n * a)
        return
    result = (n // m) * b
    n %= m
    result += min((n * a), b)
    print(result)


if __name__ == '__main__':
    main()
