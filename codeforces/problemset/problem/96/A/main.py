# https://codeforces.com/problemset/problem/96/A

def main():
    team = input()
    if '0000000' in team or '1111111' in team:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()
