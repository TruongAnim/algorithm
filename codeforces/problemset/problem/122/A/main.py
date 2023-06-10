# https://codeforces.com/problemset/problem/122/A

def main():
    numbers = int(input())
    lucky = [4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744, 747, 774, 777]
    for i in lucky:
        if numbers % i == 0:
            print('YES')
            return
    print('NO')


if __name__ == '__main__':
    main()
