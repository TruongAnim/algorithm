# https://codeforces.com/problemset/problem/510/A

def main():
    n, m = map(int, input().split(' '))
    is_right = True
    for i in range(n):
        if i % 2 == 0:
            print('#' * m)
        else:
            if is_right:
                print('.' * (m - 1) + '#')
                is_right = False
            else:
                print('#' + '.' * (m - 1))
                is_right = True


if __name__ == '__main__':
    main()
