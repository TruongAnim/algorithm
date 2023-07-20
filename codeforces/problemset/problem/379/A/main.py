# https://codeforces.com/problemset/problem/379/A

def main():
    a, b = map(int, input().split(' '))
    remain = 0
    result = 0
    while a > 0:
        result += a
        remain += a
        a = remain // b
        remain = remain % b
        # print(a)
    print(result)


if __name__ == '__main__':
    main()
