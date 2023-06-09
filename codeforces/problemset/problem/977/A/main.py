# https://codeforces.com/problemset/problem/977/A

def main():
    number, k = map(int, input().split(' '))
    for i in range(k):
        if number % 10 == 0:
            number = number // 10
        else:
            number -= 1
    print(number)


if __name__ == '__main__':
    main()
