# https://codeforces.com/contest/2009/problem/A


def main():
    t = int(input())
    for i in range(t):
        a,b = map(int, input().split(' '))
        _min = b
        for i in range(a,b+1):
            temp = (i-a)+(b-i)
            _min = min(_min,temp)
        print(_min)


if __name__ == '__main__':
    main()
