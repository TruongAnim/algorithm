# https://codeforces.com/problemset/problem/271/A

def main():
    year = int(input())
    for i in range(year + 1, 10000):
        if check_distinct(str(i)):
            print(i)
            return


def check_distinct(number):
    return len(number) == len(set(number))


if __name__ == '__main__':
    main()
