# https://codeforces.com/problemset/problem/580/A

def main():
    n = int(input())
    money = list(map(int, input().split(' ')))
    maxx = 1
    count = 1
    for i in range(1, n):
        if money[i] >= money[i - 1]:
            count += 1
            if maxx < count:
                maxx = count
        else:
            count = 1
    print(maxx)


if __name__ == '__main__':
    main()
