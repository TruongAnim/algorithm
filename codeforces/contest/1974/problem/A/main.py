# https://codeforces.com/contest/1974/problem/A

def main():
    test = int(input())
    for _ in range(test):
        a, b = map(int, input().split(' '))
        screens = b // 2 + b % 2
        du = 15 * screens - b * 4
        if a <= du:
            # print("1")
            print(screens)
        else:
            a = a - du
            # print("2")
            # print("hehe", a)
            need = a // 15 + (1 if a % 15 != 0 else 0)
            print(screens + need)


if __name__ == '__main__':
    main()
