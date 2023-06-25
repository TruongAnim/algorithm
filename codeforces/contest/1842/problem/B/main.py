# https://codeforces.com/contest/1842/problem/B


def main():
    testcase = int(input())
    for _ in range(testcase):
        n, x = map(int, input().split(' '))
        a = list(map(int, input().split(' ')))[::-1]
        b = list(map(int, input().split(' ')))[::-1]
        c = list(map(int, input().split(' ')))[::-1]
        result = 0
        while result != x:
            check = False
            for i in (a, b, c):
                if len(i) > 0:
                    last = i[-1]
                    if x | last == x:
                        result = result | last
                        i.pop()
                        check = True
                        break
            if not check:
                break
        if result == x:
            print('Yes')
        else:
            print('No')


if __name__ == '__main__':
    main()
