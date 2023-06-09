# https://codeforces.com/problemset/problem/228/A

def main():
    a, b, c, d = map(int, input().split(' '))
    s = set([a, b, c, d])
    print(4 - len(s))


if __name__ == '__main__':
    main()
