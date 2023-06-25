# https://codeforces.com/problemset/problem/431/A

def main():
    a = list(map(int, input().split(' ')))
    s = input()
    print(sum(a[ord(i) - ord('1')] for i in s))


if __name__ == '__main__':
    main()
