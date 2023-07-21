# https://codeforces.com/contest/1847/problem/B

def main():
    test = int(input())
    for _ in range(test):
        n, c = map(int, input().split(' '))
        a = tuple(map(int, input().split(' ')))
        print(binary_search(a, c))


def binary_search(a, c):
    left = 0
    right = c - get_c(a, 0, c)
    while left <= right:
        # print(left, right)
        mid = (left + right) // 2
        result = get_c(a, mid, c)
        if result == c:
            return mid
        elif result < c:
            left = mid + 1
        else:
            right = mid - 1


def get_c(a, w, c):
    s = 0
    for i in a:
        s += (i + w + w) ** 2
        if s > c:
            return 10 ** 20
    return s


if __name__ == '__main__':
    main()
