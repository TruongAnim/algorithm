# https://codeforces.com/contest/1977/problem/A

def main():
    test = int(input())
    for _ in range(test):
        a, b = map(int, input().split(' '))
        if a < b:
            print("NO")
        elif a == b:
            print("YES")
        elif (a - b) % 2 == 0:
            print("YES")
        else:
            print("NO")


if __name__ == '__main__':
    main()
