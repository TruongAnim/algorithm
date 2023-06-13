# https://codeforces.com/problemset/problem/1335/A

def main():
    testcase = int(input())
    for _ in range(testcase):
        n = int(input())
        if n % 2 == 0:
            n -= 1
        mid = n / 2
        midd = n // 2
        if mid > midd and midd > 0:
            print(midd)
        else:
            print(0)


if __name__ == '__main__':
    main()
