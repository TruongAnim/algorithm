# https://codeforces.com/problemset/problem/1669/A

def main():
    test = int(input())
    for _ in range(test):
        n = int(input())
        if n <= 1399:
            print('Division 4')
        elif n <= 1599:
            print('Division 3')
        elif n <= 1899:
            print('Division 2')
        else:
            print('Division 1')


if __name__ == '__main__':
    main()
