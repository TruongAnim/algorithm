# https://codeforces.com/contest/1844/problem/B

def main():
    testcase = int(input())
    for _ in range(testcase):
        n = int(input())
        for i in range(2, n + 1, 2):
            print(i, end=' ')
        print(1, end=' ')
        temp = [i for i in range(3, n + 1, 2)]
        for i in temp[::-1]:
            print(i, end=' ')
        print()


if __name__ == '__main__':
    main()