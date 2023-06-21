# https://codeforces.com/problemset/problem/32/B

def main():
    s = input()
    while s:
        if s[0] == '.':
            s = s[1:]
            print('0', end='')
        elif s[1] == '.':
            s = s[2:]
            print('1', end='')
        else:
            s = s[2:]
            print('2', end='')


if __name__ == '__main__':
    main()
