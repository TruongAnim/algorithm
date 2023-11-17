# https://codeforces.com/contest/1859/problem/B


def main():
    test = int(input())
    for _ in range(test):
        n = int(input())
        aa = []
        for i in range(n):
            m = int(input())
            a = sorted(map(int, input().split(' ')))
            aa.append(a)
        if n == 1:
            print(aa[0][0])
            continue
        b = []
        for i in aa:
            b.append((i[0], i[1]))

        def custom_sort(pair):
            return pair[1], pair[0]

        b = sorted(b, key=custom_sort)[::-1]
        result = 0
        _min = 10 ** 10
        for i in range(n - 1):
            result += b[i][1]
            _min = min(b[i][0], _min)
        result += min(_min, b[-1][0])
        print(result)


if __name__ == '__main__':
    main()
