# https://codeforces.com/contest/1845/problem/A

def main():
    test = int(input())
    for _ in range(test):
        n, d, h = map(int, input().split(' '))
        y = tuple(map(int, input().split(' ')))
        result = (1 / 2) * d * h
        for i in range(n - 1):
            diff = y[i + 1] - y[i]
            result += calculate_area(d, h, diff)[1]
        print(result)


def calculate_area(b, h, x):
    area = (1 / 2) * b * h
    if x >= h:
        return 0, area
    x = h - x
    upper = (x / h) ** 2 * area
    lower = area - upper
    return upper, lower


if __name__ == '__main__':
    main()
