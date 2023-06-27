# https://codeforces.com/problemset/problem/1360/A

def main():
    test = int(input())
    for _ in range(test):
        a, b = map(int, input().split(' '))
        a1 = min(a, b)
        b1 = max(a, b)
        c = max(2 * a1, b1)
        print(c * c)


if __name__ == '__main__':
    main()
