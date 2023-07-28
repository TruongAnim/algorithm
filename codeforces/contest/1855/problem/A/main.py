# https://codeforces.com/contest/1855/problem/A

def main():
    test = int(input())
    for _ in range(test):
        n = int(input())
        p = list(map(int, input().split(' ')))
        result = 0
        for i in range(n):
            if i + 1 == p[i]:
                result += 1

        print(result // 2 if result % 2 == 0 else result // 2 + 1)


if __name__ == '__main__':
    main()
