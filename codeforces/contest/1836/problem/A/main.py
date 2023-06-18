# https://codeforces.com/contest/1836/problem/A

def main():
    testcase = int(input())
    for _ in range(testcase):
        n = int(input())
        l = list(map(int, input().split(' ')))
        a = [0 for i in range(max(l) + 1)]
        for i in l:
            a[i] += 1
        for i in range(max(l)):
            if a[i] < a[i + 1]:
                print('NO')
                break
        else:
            print('YES')


if __name__ == '__main__':
    main()
