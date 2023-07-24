# https://codeforces.com/contest/1851/problem/B
# not resolve

def main():
    test = int(input())
    for _ in range(test):
        n = int(input())
        a = list(map(int, input().split(' ')))
        b = sorted([i for i in a if i % 2 == 0])
        c = sorted([i for i in a if i % 2 == 1])
        d = a[::]
        chan = 0
        le = 0
        for i in range(len(d)):
            if d[i] % 2 == 0:
                d[i] = b[chan]
                chan += 1
            else:
                d[i] = c[le]
                le += 1
        oke = True
        for i in range(len(d) - 1):
            if d[i] > d[i + 1]:
                oke = False
        if oke:
            print('YES')
        else:
            print('NO')


def check(n1, n2, k):
    pre1 = n1
    pre2 = n2
    a = [n1, n2]
    while k > 2:
        n3 = pre1 - pre2
        a.append(n3)
        if n3 > pre2 or n3 < 0:
            return False
        else:
            pre1 = pre2
            pre2 = n3
        k -= 1
    print(a)
    print(sum(a))
    return True


if __name__ == '__main__':
    main()
