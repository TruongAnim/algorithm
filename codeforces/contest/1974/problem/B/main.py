# https://codeforces.com/contest/1974/problem/B


def get_char(s, c):
    index = s.index(c)
    return s[len(s) - index - 1]


def main():
    import sys
    sys.stdin = open('input.txt', 'r')
    test = int(input())
    for _ in range(test):
        l = int(input())
        s = input()
        r = sorted(list(set(s)))
        decode = [get_char(r, i) for i in s]
        print(''.join(decode))


if __name__ == '__main__':
    main()
