# https://codeforces.com/problemset/problem/405/A

def main():
    n = int(input())
    h = list(map(int, input().split(' ')))
    l = [0 for i in range(101)]
    l2 = [0 for i in range(n)]
    for i in range(101):
        s = 0
        for j in h:
            if j >= i + 1:
                s += 1
        l[i] = s
    for i in range(n):
        s = 0
        for j in l:
            if j >= n - i:
                s += 1
        l2[i] = s
    for i in l2:
        print(i, end=' ')


if __name__ == '__main__':
    main()
