# https://codeforces.com/problemset/problem/112/A

def main():
    import sys
    sys.stdin = open('input.txt', 'r')
    str1 = input().lower()
    str2 = input().lower()
    if str1 < str2:
        print(-1)
    elif str1 > str2:
        print(1)
    else:
        print(0)


if __name__ == '__main__':
    main()
