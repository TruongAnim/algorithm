# https://codeforces.com/contest/1948/problem/A

def main():
    test = int(input())
    for _ in range(test):
        n = int(input())
        if n % 2 != 0:
            print('NO')
        else:
            print('YES')
            for i in range(n // 2):
                print('AAB', end='')
            print()

if __name__ == '__main__':
    main()
