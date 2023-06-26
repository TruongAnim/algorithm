# https://codeforces.com/problemset/problem/1624/A

def main():
    testcase = int(input())
    for _ in range(testcase):
        n = int(input())
        a = tuple(map(int, input().split(' ')))
        print(max(a) - min(a))


if __name__ == '__main__':
    main()
