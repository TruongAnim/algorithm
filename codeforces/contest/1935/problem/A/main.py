# https://codeforces.com/contest/1935/problem/A

def main():
    test = int(input())
    a = []
    for _ in range(test):
        n = input()
        _0 = 0
        _1 = 0
        for i in n:
            if i == '0':
                _0 += 1
            else:
                _1 += 1
        a.append((_0, _1))


if __name__ == '__main__':
    main()
