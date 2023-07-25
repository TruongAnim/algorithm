# https://codeforces.com/contest/1851/problem/C
# not resolve

def main():
    test = int(input())
    for _ in range(test):
        n, k = map(int, input().split(' '))
        colors = tuple(map(int, input().split(' ')))
        count = 0
        need1 = colors[0]
        need2 = colors[-1]
        first = -1
        for i in range(n):
            if colors[i] == need1:
                count += 1
                if count == k:
                    first = i
                    break
        if first < 0:
            print('NO')
            continue
        if need1 == need2:
            print('YES')
            continue
        count2 = 0
        oke = False
        for i in range(first + 1, n):
            if colors[i] == need2:
                count2 += 1
                if count2 == k:
                    oke = True
                    break
        if oke:
            print('YES')
        else:
            print('NO')


if __name__ == '__main__':
    main()
