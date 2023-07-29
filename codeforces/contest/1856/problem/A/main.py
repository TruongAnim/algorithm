# https://codeforces.com/contest/1856/problem/A

def main():
    test = int(input())
    for _ in range(test):
        n = int(input())
        p = list(map(int, input().split(' ')))
        result = 0
        for i in range(n - 1):
            if p[i] > p[i + 1]:
                result = max(result, p[i])
        print(result)


if __name__ == '__main__':
    main()
