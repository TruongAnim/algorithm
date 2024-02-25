# https://codeforces.com/contest/1926/problem/B

def main():
    test = int(input())
    for _ in range(test):
        n = int(input())
        a = list(map(int, input().split(' ')))
        s = sum(a)
        tb = s // n
        if tb * n != s:
            print('NO')
            continue
        du = 0
        check = True
        for i in a:
            if i < tb:
                du -= tb - i
            if i > tb:
                du += i - tb
            if du < 0:
                check = False
                break
        if not check:
            print('NO')
            continue
        else:
            print('YES')


if __name__ == '__main__':
    main()
