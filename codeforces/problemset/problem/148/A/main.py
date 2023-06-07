# https://codeforces.com/problemset/problem/148/A

def main():
    k = int(input())
    l = int(input())
    m = int(input())
    n = int(input())
    d = int(input())
    sum = 0
    for i in range(1, d + 1):
        if i % k == 0 or i % l == 0 or i % m == 0 or i % n == 0:
            sum += 1
    print(sum)


if __name__ == '__main__':
    main()
