# https://codeforces.com/contest/1851/problem/D


def main():
    test = int(input())
    for _ in range(test):
        n = int(input())
        a = list(map(int, ('0 ' + input()).split(' ')))
        m = {}
        for i in range(1, n):
            diff = a[i] - a[i - 1]
            if diff <= 0:
                break
            if diff not in m:
                m[diff] = 1
            else:
                m[diff] += 1
        miss = []
        for i in range(1, n + 1):
            if i not in m:
                miss.append(i)
        thua = []
        for i in m.keys():
            if m[i] > 1 or i > n:
                thua.append(i)
        if (len(thua) == 1 and len(miss) == 2 and thua[0] == sum(miss)) or (len(thua) == 0 and len(miss) == 1):
            print('YES')
        else:
            print('NO')


if __name__ == '__main__':
    main()
