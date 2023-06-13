# https://codeforces.com/problemset/problem/492/B

def main():
    n, l = map(int, input().split(' '))
    a = sorted(list(map(int, input().split(' '))))
    start = 0
    diff = 0
    for i in a:
        if (i - start) > diff:
            diff = (i - start)
        start = i
    result = diff / 2
    if result < a[0]:
        result = a[0]
    if result < (l - start):
        result = (l - start)
    print(result)


if __name__ == '__main__':
    main()
