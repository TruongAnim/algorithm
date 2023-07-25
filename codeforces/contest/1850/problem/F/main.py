# https://codeforces.com/contest/1850/problem/F
# not resolve

def main():
    test = int(input())
    for _ in range(test):
        n = int(input())
        a = tuple(i for i in map(int, input().split(' ')) if i <= n)
        _max = 0
        for i in range(n):
            _max = max(get_frog(a, i + 1), _max)
        print(_max)


def get_frog(a, n):
    result = 0
    for i in a:
        if n % i == 0:
            result += 1
    return result


if __name__ == '__main__':
    main()
