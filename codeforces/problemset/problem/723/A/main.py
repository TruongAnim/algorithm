# https://codeforces.com/problemset/problem/723/A

def main():
    a, b, c = map(int, input().split(' '))
    _min = min(a, b, c)
    _max = max(a, b, c)
    print(_max - _min)


if __name__ == '__main__':
    main()
