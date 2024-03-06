# https://codeforces.com/contest/1930/problem/A

def main():
    test = int(input())
    for i in range(test):
        n = int(input())
        a = sorted(list(map(int, input().split(' '))))[::-1]
        print(sum(a[1::2]))


if __name__ == '__main__':
    main()
