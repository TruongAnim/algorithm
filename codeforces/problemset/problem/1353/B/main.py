# https://codeforces.com/problemset/problem/1353/B

def main():
    test = int(input())
    for _ in range(test):
        n, k = map(int, input().split(' '))
        a = sorted(map(int, input().split(' ')))
        b = sorted(map(int, input().split(' ')))[::-1]
        c = [max(a[i], b[i]) for i in range(k)]
        print(sum(a[k:]) + sum(c[:k]))


if __name__ == '__main__':
    main()
