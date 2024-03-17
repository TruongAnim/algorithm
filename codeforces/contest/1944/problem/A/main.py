# https://codeforces.com/contest/1944/problem/A

def main():
    test = int(input())
    for _ in range(test):
        n, k = map(int, input().split(' '))
        if k >= n - 1:
            print(1)
        else:
            print(n)


if __name__ == '__main__':
    main()
