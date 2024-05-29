# https://codeforces.com/contest/1971/problem/A

def main():
    test = int(input())
    for _ in range(test):
        a, b = map(int, input().split(' '))
        print(min(a,b), max(a,b))


if __name__ == '__main__':
    main()
