# https://codeforces.com/problemset/problem/1367/B


def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(map(int, input().split(' ')))
        error_odd, error_even = 0, 0
        for i, j in enumerate(a):
            if i % 2 == 0 and j % 2 == 1:
                error_odd += 1
            if i % 2 == 1 and j % 2 == 0:
                error_even += 1
        print(-1) if error_even != error_odd else print(error_even)


if __name__ == '__main__':
    main()
