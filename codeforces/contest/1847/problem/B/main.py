# https://codeforces.com/contest/1847/problem/B

def main():
    test = int(input())
    for _ in range(test):
        n = int(input())
        a = tuple(map(int, input().split(' ')))
        _max = a[0]
        result = 0
        for i in a:
            _max &= i
        if _max != 0:
            print(1)
            continue
        i = 0
        while i < n:
            temp = a[i]
            for j in range(i, n):
                temp &= a[j]
                if temp <= _max:
                    result += 1
                    i = j
                    break
                if j == n - 1:
                    break
            i += 1
        print(result)


if __name__ == '__main__':
    main()