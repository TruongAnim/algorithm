# https://codeforces.com/problemset/problem/339/B

def main():
    n, m = map(int, input().split(' '))
    a = tuple(map(int, input().split(' ')))
    total = a[0] - 1
    pre = a[0]
    for i in a[1:]:
        if i >= pre:
            total += i - pre
            pre = i
        else:
            total += n - (pre - i)
            pre = i
    print(total)


if __name__ == '__main__':
    main()
