# https://codeforces.com/contest/1941/problem/A

def main():
    test = int(input())
    for _ in range(test):
        n, m, k = map(int, input().split(' '))

        b = list(map(int, input().split(' ')))
        c = list(map(int, input().split(' ')))
        s = 0
        for i in b:
            for j in c:
                if i + j <= k:
                    s += 1
        print(s)


if __name__ == '__main__':
    main()
