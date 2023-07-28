# https://codeforces.com/contest/1855/problem/B


def main():
    test = int(input())
    for _ in range(test):
        n = int(input())
        for i in range(1, n + 2):
            if n % i != 0:
                print(i - 1)
                break


if __name__ == '__main__':
    main()
