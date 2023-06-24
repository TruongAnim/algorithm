# https://codeforces.com/problemset/problem/500/A

def main():
    n, t = map(int, input().split(' '))
    a = tuple(map(int, input().split(' ')))
    i = 1
    while i < t:
        i += a[i - 1]
        # print(i)
    if i == t:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()
