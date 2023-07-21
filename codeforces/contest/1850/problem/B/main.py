# https://codeforces.com/contest/1850/problem/B

def main():
    test = int(input())
    for _ in range(test):
        n = int(input())
        a = []
        for i in range(n):
            x, y = map(int, input().split(' '))
            if x <= 10:
                a.append([y, i])
        print(sorted(a)[-1][1] + 1)


if __name__ == '__main__':
    main()
