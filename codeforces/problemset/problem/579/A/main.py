# https://codeforces.com/problemset/problem/579/A

def main():
    x = int(input())
    print(need(x))


def need(x):
    for i in range(100):
        if 2 ** i == x:
            return 1
        elif 2 ** i > x:
            return 1 + need(x - (2 ** (i - 1)))


if __name__ == '__main__':
    main()
