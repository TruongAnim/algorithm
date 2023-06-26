# https://codeforces.com/problemset/problem/1433/A

def main():
    test = int(input())
    for _ in range(test):
        n = input()
        n_int = int(n[0])
        print((n_int - 1) * 10 + get_sum(n))


def get_sum(n):
    return sum(i for i in range(len(n) + 1))


if __name__ == '__main__':
    main()
