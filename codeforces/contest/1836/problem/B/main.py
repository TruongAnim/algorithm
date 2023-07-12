# https://codeforces.com/contest/1836/problem/B

def main():
    testcase = int(input())
    for _ in range(testcase):
        n, k, g = map(int, input().split(' '))
        total = k * g
        each = g // 2 - 1 if g % 2 == 0 else g // 2
        all = each * (n - 1)
        remain = total - all
        # print(total, each, all, remain)
        print(total - get_r(remain, g, each))


def get_r(x, g, each):
    if x < 0:
        return 0
    r = x % g
    if r >= each + 1:
        return x + (g - r)
    else:
        return x - r


if __name__ == '__main__':
    main()
