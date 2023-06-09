# https://codeforces.com/problemset/problem/116/A

def main():
    import sys
    sys.stdin = open('input.txt', 'r')
    n = int(input())
    capacity = 0
    max = 0
    for i in range(n):
        exit, enter = map(int, input().split(' '))
        capacity -= exit
        capacity += enter
        if max < capacity:
            max = capacity
    print(max)


if __name__ == '__main__':
    main()
