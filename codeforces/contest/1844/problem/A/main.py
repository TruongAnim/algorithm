# https://codeforces.com/contest/1844/problem/A

def main():
    testcase = int(input())
    for _ in range(testcase):
        a, b = map(int, input().split(' '))
        if a == 1 and b > 2:
            print(2)
        if a == 1 and b == 2:
            print(3)
        if a != 1:
            print(1)


if __name__ == '__main__':
    main()
