# https://codeforces.com/contest/1907/problem/A

def main():
    test = int(input())
    for i in range(test):
        s = input()
        x = s[0]
        y = s[1]
        temp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        for i in range(1, 9):
            if i != int(y):
                print(x, i, sep='')
        for i in temp:
            if i != x:
                print(i, y, sep='')


if __name__ == '__main__':
    main()