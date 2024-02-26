# https://codeforces.com/contest/1923/problem/B

def main():
    import sys
    sys.stdin = open('input.txt', 'r')
    test = int(input())
    for _ in range(test):
        n, k = map(int, input().split(' '))
        a = list(map(int, input().split(' ')))
        x = list(map(int, input().split(' ')))
        M = {}
        for i in range(n):
            if x[i] < 0:
                x[i] = -x[i]
            if x[i] not in M:
                M[x[i]] = 0
            M[x[i]] += a[i]
        a = [[i, M[i]] for i in M.keys()]
        a = sorted(a, key=lambda x: -x[0])
        bullet = k
        turn = 1
        is_oke = False
        while True:
            last = a[-1]
            # print(last, turn, bullet)
            if last[1] <= bullet:
                bullet -= last[1]
                a.pop()
            else:
                last[1] -= bullet
                bullet = 0
            if len(a) == 0:
                is_oke = True
                break
            if a[-1][0] <= turn:
                break
            turn += 1
            bullet += k
        if is_oke:
            print('YES')
        else:
            print('NO')


if __name__ == '__main__':
    main()
