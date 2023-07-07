# https://codeforces.com/contest/1846/problem/A

def main():
    test = int(input())
    for _ in range(test):
        n = int(input())
        result = 0
        for i in range(n):
            a, b = map(int, input().split(' '))
            if a - b > 0:
                result += 1
        print(result)


if __name__ == '__main__':
    main()
