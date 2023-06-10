# https://codeforces.com/problemset/problem/158/B

def main():
    n = int(input())
    children = list(map(int, input().split(' ')))
    m = {i: 0 for i in range(5)}
    result = 0
    for i in children:
        m[i] += 1
    result += get(m, (3, 1), (1, 1))
    result += get(m, (2, 2), (0, 0))
    result += get(m, (2, 1), (1, 2))
    result += get(m, (2, 1), (1, 1))
    result += get(m, (1, 4), (0, 0))
    result += get(m, (1, 3), (0, 0))
    result += get(m, (1, 2), (0, 0))

    for i in range(1, 5):
        result += m[i]
    print(result)


def get(m, a, b):
    s = 0
    while m[a[0]] >= a[1] and m[b[0]] >= b[1]:
        s += 1
        m[a[0]] -= a[1]
        m[b[0]] -= b[1]
    return s


if __name__ == '__main__':
    main()
