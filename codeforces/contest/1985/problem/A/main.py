# https://codeforces.com/contest/1985/problem/A

def main():
    test = int(input())
    for _ in range(test):
        a,b = input().split(' ')
        print(b[0]+a[1:], a[0]+b[1:])


if __name__ == '__main__':
    main()
