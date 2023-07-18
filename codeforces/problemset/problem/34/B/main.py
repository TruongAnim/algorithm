# https://codeforces.com/problemset/problem/34/B

def main():
    n, m = map(int, input().split(' '))
    a = sorted(i for i in list(map(int, input().split(' '))) if i < 0)
    print(sum(a[0: m]) * -1)


if __name__ == '__main__':
    main()
