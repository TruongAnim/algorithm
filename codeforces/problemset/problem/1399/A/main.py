# https://codeforces.com/problemset/problem/1399/A

def main():
    testcase = int(input())
    for _ in range(testcase):
        n = int(input())
        a = sorted(map(int, input().split(' ')))
        if len(a) == 1:
            print('YES')
            continue
        yes = abs(a[0] - a[1]) <= 1 and abs(a[n - 1] - a[n - 2]) <= 1
        for i in range(1, n - 1):
            if not (abs(a[i] - a[i - 1]) <= 1 and abs(a[i] - a[i + 1]) <= 1):
                yes = False
                break
        print('YES' if yes else 'NO')


if __name__ == '__main__':
    main()
