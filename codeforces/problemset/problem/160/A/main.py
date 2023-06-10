# https://codeforces.com/problemset/problem/160/A

def main():
    n = int(input())
    coins = list(map(int, input().split(' ')))
    coins = sorted(coins)[::-1]
    total = sum(coins)
    yours = 0
    for i in range(len(coins)):
        yours += coins[i]
        if yours > total / 2:
            print(i + 1)
            return
    print(1)


if __name__ == '__main__':
    main()
