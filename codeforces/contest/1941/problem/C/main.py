# https://codeforces.com/contest/1941/problem/C


def main():
    import sys
    sys.stdin = open('input.txt', 'r')
    test = int(input())
    for _ in range(test):
        n = int(input())
        a = input()
        b = [0 for i in range(n)]
        for i in range(n - 4):
            if a[i:i + 5] == 'mapie':
                b[i + 2] = 1
        bb = []
        for i in range(n):
            if b[i] == 0:
                bb.append(a[i])
        a = ''.join(bb)
        print(a)
        b = [0 for i in range(len(a))]
        count = 0
        for i in range(len(a)):
            if a[i:i + 3] == 'pie' or a[i:i + 3] == 'map':
                count += 1
        print(n - len(a) + count)


if __name__ == '__main__':
    main()
