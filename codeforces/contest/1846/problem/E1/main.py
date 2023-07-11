# https://codeforces.com/contest/1846/problem/E1

def main():
    f = 10**6
    a = set()
    k = 1000
    for i in range(2, k):
        start = 1
        for j in range(1, k):
            start += i ** j
            if start > f:
                break
            if j >= 2:
                a.add(start)
    test = int(input())
    for _ in range(test):
        n = int(input())
        if n in a:
            print('YES')
        else:
            print('NO')


if __name__ == '__main__':
    main()
