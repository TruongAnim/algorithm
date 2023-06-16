# https://codeforces.com/problemset/problem/1154/A

def main():
    s1, s2, s3, s4 = sorted(map(int, input().split(' ')))
    a = s4 - s1
    b = s4 - s2
    c = s4 - s3
    print(a, b, c)


if __name__ == '__main__':
    main()
