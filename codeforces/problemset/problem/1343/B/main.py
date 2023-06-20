# https://codeforces.com/problemset/problem/1343/B

def main():
    testcase = int(input())
    for _ in range(testcase):
        n = int(input())
        if (n // 2) % 2 == 0:
            print('YES')
            for i in range(2, 2 * (n // 2) + 1, 2):
                print(i, end=' ')
            for i in range(1, 2 * (n // 2), 2):
                if i == 2 * (n // 2) - 1:
                    print(i + (n // 2), end=' ')
                else:
                    print(i, end=' ')
            print()
        else:
            print('NO')


if __name__ == '__main__':
    main()
