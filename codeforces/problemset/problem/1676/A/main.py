# https://codeforces.com/problemset/problem/1676/A

def main():
    n = int(input())
    for i in range(n):
        s = input()
        if get_sum(s[:3]) == get_sum(s[3:]):
            print('YES')
        else:
            print('NO')


def get_sum(s):
    return sum([int(i) for i in s])


if __name__ == '__main__':
    main()
