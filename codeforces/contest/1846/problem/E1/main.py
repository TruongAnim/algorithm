# https://codeforces.com/contest/1845/problem/A

def main():
    f = 10**18
    a = set()
    k = 1000000
    for i in range(2, k):
        start = 1
        for j in range(1, k):
            start += i ** j
            if start > f:
                break
            if j >= 2:
                a.add(start)
    # print(a)
    print(len(a))
    test = int(input())
    for _ in range(test):
        n = int(input())
        if n in a:
            print('YES')
        else:
            print('NO')


if __name__ == '__main__':
    main()
