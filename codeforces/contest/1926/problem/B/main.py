# https://codeforces.com/contest/1926/problem/B

def main():
    test = int(input())
    for _ in range(test):
        n = int(input())
        is_tri = False
        for t in range(n):
            temp = input()
            for i in range(1, n - 1):
                if temp[i] == '1' and temp[i - 1] == '0' and temp[i + 1] == '0':
                    is_tri = True
        if is_tri:
            print('TRIANGLE')
        else:
            print('SQUARE')


if __name__ == '__main__':
    main()