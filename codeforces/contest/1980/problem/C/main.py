# https://codeforces.com/contest/1980/problem/C

def main():
    import sys
    sys.stdin = open('input.txt', 'r')
    test = int(input())
    A = [2 ** i for i in range(32)]
    for _ in range(test):
        n = int(input())
        a = list(map(int, input().split(' ')))
        b = list(map(int, input().split(' ')))
        m = int(input())
        d = list(map(int, input().split(' ')))
        if _ == 10:
            print(a,b)
        contain = set(b)
        needs = {}
        has = {}
        for i, j in zip(a, b):
            if i != j:
                if j not in needs:
                    needs[j] = 0
                needs[j] += 1
        for i in d:
            if i not in has:
                has[i] = 0
            has[i] += 1
        is_oke = True
        for i in d:
            if i not in contain:
                is_oke = False
            else:
                is_oke = True
        for i, j in zip(a, b):
            if i != j:
                if j in has and has[j] > 0:
                    has[j] -= 1
                else:
                    is_oke = False

        print('YES') if is_oke else print('NO')


if __name__ == '__main__':
    main()
