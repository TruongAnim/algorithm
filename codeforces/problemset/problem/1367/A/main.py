# https://codeforces.com/problemset/problem/1367/A

def main():
    n = int(input())
    for _ in range(n):
        s = input()
        result = ''
        for i in range(0, len(s), 2):
            result += s[i]
        print(result + s[-1])


if __name__ == '__main__':
    main()
