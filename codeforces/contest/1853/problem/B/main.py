# https://codeforces.com/contest/1853/problem/B
# not resolve

def main():
    test = int(input())
    for _ in range(test):
        n, k = map(int, input().split(' '))
        result = 0
        for i in range(1, n + 1):
            if check(n, i, k):
                result += 1
        print(result)


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
