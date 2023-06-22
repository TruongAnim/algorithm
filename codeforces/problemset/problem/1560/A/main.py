# https://codeforces.com/problemset/problem/1560/A

def main():
    a = [i for i in range(1, 10000) if i % 3 != 0 and i % 10 != 3]
    t = int(input())
    for i in range(t):
        k = int(input())
        print(a[k - 1])


if __name__ == '__main__':
    main()
