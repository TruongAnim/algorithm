# https://codeforces.com/problemset/problem/1760/A

def main():
    test = int(input())
    for _ in range(test):
        a = sorted(map(int, input().split(' ')))
        print(a[1])


if __name__ == '__main__':
    main()
