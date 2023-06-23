# https://codeforces.com/problemset/problem/1475/A

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        if n % 2 == 1:
            print('YES')
        else:
            while n % 2 == 0:
                n /= 2
            if n != 1:
                print('YES')
            else:
                print('NO')


if __name__ == '__main__':
    main()
