# https://codeforces.com/problemset/problem/1722/A

def main():
    a = int(input())
    for i in range(a):
        b = input()
        c = input()
        if b == '5' and 'T' in c and 'i' in c and 'm' in c and 'u' in c and 'r' in c:
            print('YES')
        else:
            print('NO')


if __name__ == '__main__':
    main()
