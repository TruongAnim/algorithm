# https://codeforces.com/problemset/problem/133/A

def main():
    s = input()
    for i in s:
        if i in ['H', 'Q', '9']:
            print('YES')
            return
    print('NO')


if __name__ == '__main__':
    main()
