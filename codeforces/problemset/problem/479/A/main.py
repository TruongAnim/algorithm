# https://codeforces.com/problemset/problem/479/A

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    a = [a * b * c, a + b * c, a + b + c, a * b + c, (a + b) * c, a * (b + c)]
    print(max(a))


if __name__ == '__main__':
    main()
