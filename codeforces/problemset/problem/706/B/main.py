# https://codeforces.com/problemset/problem/706/B
import bisect


def main():
    n = int(input())
    x = tuple(sorted(map(int, input().split(' '))))
    q = int(input())
    for i in range(q):
        a = int(input())
        index = bisect.bisect_right(x, a)
        print(index)


if __name__ == '__main__':
    main()
