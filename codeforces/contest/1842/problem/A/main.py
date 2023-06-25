# https://codeforces.com/contest/1842/problem/A

def main():
    testcase = int(input())
    for _ in range(testcase):
        n, m = map(int, input().split(' '))
        a = list(map(int, input().split(' ')))
        b = list(map(int, input().split(' ')))
        if sum(a) > sum(b):
            print('Tsondu')
        elif sum(a) < sum(b):
            print('Tenzing')
        else:
            print('Draw')


if __name__ == '__main__':
    main()
