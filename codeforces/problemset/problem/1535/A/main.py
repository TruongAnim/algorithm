# https://codeforces.com/problemset/problem/1535/A

def main():
    n = int(input())
    for i in range(n):
        a = list(map(int, input().split(' ')))
        b = sorted(a)
        if b[-1] in a[0:2] and b[-2] in a[2:]:
            print('YES')
            continue
        if b[-2] in a[0:2] and b[-1] in a[2:]:
            print('YES')
            continue
        print('NO')


if __name__ == '__main__':
    main()
