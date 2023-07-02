# https://codeforces.com/problemset/problem/1619/A

def main():
    test = int(input())
    for _ in range(test):
        s = input()
        l = len(s)
        if s[:l // 2] == s[l // 2:] and l % 2 == 0:
            print('YES')
        else:
            print('NO')


if __name__ == '__main__':
    main()
