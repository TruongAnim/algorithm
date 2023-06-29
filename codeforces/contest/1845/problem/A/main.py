# https://codeforces.com/contest/1845/problem/A

def main():
    test = int(input())
    for _ in range(test):
        n, k, x = map(int, input().split(' '))
        if x != 1:
            print('YES')
            print(n)
            print(' '.join(['1'] * n))
        else:
            # x = 1
            if k == 1:
                print('NO')
            elif k == 2:
                if n % 2 == 0:
                    print('YES')
                    print(n // 2)
                    print(' '.join(['2'] * (n // 2)))
                else:
                    print('NO')
            else:
                if k == n:
                    print('YES')
                    print(1)
                    print(k)
                else:
                    if n % 2 == 0:
                        print('YES')
                        print(n // 2)
                        print(' '.join(['2'] * (n // 2)))
                    else:
                        print('YES')
                        print(1 + (n - 3) // 2)
                        print('3', ' '.join(['2'] * ((n - 3) // 2)))


if __name__ == '__main__':
    main()
