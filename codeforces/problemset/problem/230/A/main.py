# https://codeforces.com/problemset/problem/230/A

def main():
    s, n = map(int, input().split(' '))
    dragons = []
    for i in range(n):
        x, y = map(int, input().split(' '))
        dragons.append([x, y])
    dragons = sorted(dragons, key=lambda i: i[0])
    for i, j in dragons:
        if s > i:
            s += j
        else:
            print('NO')
            return
    print('YES')


if __name__ == '__main__':
    main()
