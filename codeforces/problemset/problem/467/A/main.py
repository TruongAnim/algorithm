# https://codeforces.com/problemset/problem/467/A

def main():
    n = int(input())
    sum = 0
    for i in range(n):
        x, y = map(int, input().split(' '))
        if x <= y - 2:
            sum += 1
    print(sum)


if __name__ == '__main__':
    main()
