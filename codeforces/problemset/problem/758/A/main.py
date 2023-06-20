# https://codeforces.com/problemset/problem/758/A

def main():
    n = int(input())
    s = tuple(map(int, input().split(' ')))
    _max = max(s)
    result = 0
    for i in s:
        result += abs(i - _max)
    print(result)


if __name__ == '__main__':
    main()
