# https://codeforces.com/contest/1849/problem/A

def main():
    test = int(input())
    for _ in range(test):
        b, c, h = map(int, input().split(' '))
        result = 1
        b = b - 1
        result += min(b, c + h)*2
        print(result)


if __name__ == '__main__':
    main()
