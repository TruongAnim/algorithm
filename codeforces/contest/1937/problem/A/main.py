# https://codeforces.com/contest/1937/problem/A

def main():
    test = int(input())
    for _ in range(test):
        n = int(input())
        temp = 1
        while True:
            if temp <= n:
                temp *= 2
            else:
                break
        print(temp // 2)


if __name__ == '__main__':
    main()
