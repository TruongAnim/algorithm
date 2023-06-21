# https://codeforces.com/contest/1843/problem/C

def main():
    tesecase = int(input())
    for _ in range(tesecase):
        n = int(input())
        sum = 0
        while n != 0:
            sum += n
            n //= 2
        print(sum)


if __name__ == '__main__':
    main()
