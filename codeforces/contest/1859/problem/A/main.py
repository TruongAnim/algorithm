# https://codeforces.com/contest/1859/problem/A

def main():
    test = int(input())
    for _ in range(test):
        n = int(input())
        a = sorted(map(int, input().split(' ')))
        _max = max(a)
        b = [i for i in a if i != _max]
        c = [i for i in a if i == _max]
        if _max == a[0]:
            print(-1)
        else:
            print(len(b), len(c))
            for i in b:
                print(i, end=' ')
            print()
            for i in c:
                print(i, end=' ')
            print()


if __name__ == '__main__':
    main()
