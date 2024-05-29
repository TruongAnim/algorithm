# https://codeforces.com/contest/1971/problem/B

def main():
    test = int(input())
    for _ in range(test):
        s = input()
        found = False
        for i in range(len(s) - 1):
            if s[i] != s[i + 1]:
                print('YES')
                print(s[:i] + s[i + 1] + s[i] + s[i + 2:])
                found = True
                break
        if not found:
            print('NO')


if __name__ == '__main__':
    main()
