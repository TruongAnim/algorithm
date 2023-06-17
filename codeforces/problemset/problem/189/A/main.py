# https://codeforces.com/problemset/problem/189/A

def main():
    n, a, b, c = map(int, input().split(' '))
    a, b, c = sorted((a, b, c))
    if a == 1:
        print(n)
        return
    result = 0
    for i in range(0, n + 1, a):
        for j in range(0, n + 1, b):
            aa = i // a
            bb = j // b
            remainder = (n - i - j)
            if remainder % c == 0 and remainder >= 0:
                result = max(result, aa + bb + remainder // c)
    print(result)


if __name__ == '__main__':
    main()
