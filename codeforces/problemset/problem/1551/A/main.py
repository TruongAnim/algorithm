# https://codeforces.com/problemset/problem/1551/A

def main():
    test = int(input())
    for _ in range(test):
        n = int(input())
        du = n % 3
        divisor = n // 3
        if du == 0:
            print(divisor, divisor)
        if du == 1:
            print(divisor + 1, divisor)
        if du == 2:
            print(divisor, divisor + 1)


if __name__ == '__main__':
    main()
