# https://codeforces.com/contest/1926/problem/A

def main():
    test = int(input())
    for _ in range(test):
        s = input()
        c = 0
        for i in s:
            if i == 'A':
                c += 1
        if c < 3:
            print('B')
        else:
            print('A')


if __name__ == '__main__':
    main()