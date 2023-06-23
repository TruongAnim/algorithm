# https://codeforces.com/problemset/problem/1374/A

def main():
    t = int(input())
    for i in range(t):
        x, y, n = map(int, input().split(' '))
        a = (n - y) // x
        print(a * x + y)


if __name__ == '__main__':
    main()
