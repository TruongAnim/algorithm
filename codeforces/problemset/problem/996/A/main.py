# https://codeforces.com/problemset/problem/996/A

def main():
    n = int(input())
    sum = 0
    bills = [100, 20, 10, 5, 1]
    for i in bills:
        sum += n // i
        n %= i
    print(sum)


if __name__ == "__main__":
    main()
