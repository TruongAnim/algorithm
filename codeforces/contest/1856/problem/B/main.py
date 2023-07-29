# https://codeforces.com/contest/1856/problem/B


def main():
    test = int(input())
    for _ in range(test):
        n = int(input())
        a = list(map(int, input().split(' ')))
        if n == 1:
            print('NO')
            continue
        count1 = a.count(1)
        not1 = n - count1
        s = sum(item for item in a if item != 1)
        if count1 > (s - not1):
            print('NO')
        else:
            print('YES')


if __name__ == '__main__':
    main()
