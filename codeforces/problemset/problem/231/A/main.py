# https://codeforces.com/problemset/problem/231/A

def main():
    import sys
    sys.stdin = open('input.txt', 'r')
    n = int(input())
    sum = 0
    for i in range(n):
        a, b, c = map(int, input().split())
        if a + b + c > 1:
            sum += 1
    print(sum)


if __name__ == '__main__':
    main()
