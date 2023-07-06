# https://codeforces.com/contest/1847/problem/A

def main():
    test = int(input())
    for _ in range(test):
        n, k = map(int, input().split(' '))
        a = tuple(map(int, input().split(' ')))
        diff = []
        for i in range(n - 1):
            diff.append(abs(a[i] - a[i + 1]))
        diff = sorted(diff)
        print(sum(diff[:n - k]))


if __name__ == '__main__':
    main()
