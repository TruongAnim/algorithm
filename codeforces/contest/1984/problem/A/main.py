# https://codeforces.com/contest/1984/problem/A

def main():
    test = int(input())
    for _ in range(test):
        n = int(input())
        A = list(map(int, input().split(' ')))
        is_diff = False
        is_diff_2 = False
        for i in A[1:]:
            if i != A[0]:
                is_diff = True
        for i in A[2:]:
            if i != A[1]:
                is_diff_2 = True
        if is_diff:
            print('YES')
            print('R', end='')
            if is_diff_2:
                for i in range(n - 1):
                    print('B', end='')
            else:
                print('B', end='')
                for i in range(n - 2):
                    print('R', end='')
            print()
        else:
            print('NO')


if __name__ == '__main__':
    main()
