# https://codeforces.com/problemset/problem/1692/A

def main():
    n = int(input())
    for i in range(n):
        a, b, c, d = map(int, input().split(' '))
        d = sorted([a, b, c, d])
        print(4 - d.index(a) - 1)


if __name__ == '__main__':
    main()
