# https://codeforces.com/problemset/problem/791/A

def main():
    limak, bob = map(int, input().split(' '))
    year = 0
    while limak <= bob:
        year += 1
        limak *= 3
        bob *= 2
    print(year)


if __name__ == '__main__':
    main()
