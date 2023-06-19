# https://codeforces.com/problemset/problem/432/A

def main():
    n, k = map(int, input().split(' '))
    y = sorted(map(int, input().split(' ')))
    result = 0
    for i in range(0, len(y) - 2, 3):
        m = max(y[i], y[i + 1], y[i + 2])
        if m + k <= 5:
            result += 1
    print(result)


if __name__ == '__main__':
    main()
