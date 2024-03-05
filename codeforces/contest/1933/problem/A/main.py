# https://codeforces.com/contest/1933/problem/A

def main():
    test = int(input())
    for _ in range(test):
        n = input()
        a = list(map(int, input().split(' ')))
        s = 0
        for i in a:
            if i < 0:
                s += -i
            else:
                s += i
        print(s)


if __name__ == '__main__':
    main()
