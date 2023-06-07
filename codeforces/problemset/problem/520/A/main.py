# https://codeforces.com/problemset/problem/520/A

def main():
    n = int(input())
    words = input().lower()
    letters = set(words)
    if len(letters) >= 26:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()
