# https://codeforces.com/problemset/problem/546/A

def main():
    k, n, w = map(int, input().split(' '))
    sum = 0
    for i in range(w):
        sum += k * (i + 1)
    if sum <= n:
        print(0)
    else:
        print(sum - n)


if __name__ == '__main__':
    main()
