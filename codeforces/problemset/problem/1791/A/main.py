# https://codeforces.com/problemset/problem/1791/A

def main():
    test = int(input())
    for _ in range(test):
        c = input()
        if c in 'codeforces':
            print('YES')
        else:
            print('NO')


if __name__ == '__main__':
    main()
