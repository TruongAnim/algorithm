# https://codeforces.com/contest/1931/problem/E
from collections import deque


def count_trailing_zeros(n):
    count = 0

    # Iterate from the end of the string
    for digit in reversed(n):
        if digit == '0':
            count += 1
        else:
            break

    return count


def count_number(n):
    return [len(n), count_trailing_zeros(n)]


def anna_move(n):
    first = n.pop()
    n.appendleft([first[0] - first[1], 0])


def shasa_move(n):
    first = n.pop()
    second = n.pop()
    n.append([first[0] + second[0], second[1]])


def main():
    import sys
    sys.stdin = open('input.txt', 'r')
    test = int(input())
    for t in range(test):
        n, m = map(int, input().split(' '))
        a = input().split(' ')
        b = list(map(count_number, a))
        sorted_b = sorted(b, key=lambda x: x[1])
        b = deque(sorted_b)
        while True:
            anna_move(b)
            if len(b) == 1:
                break
            shasa_move(b)
        if b[0][0] > m:
            print('Sasha')
        else:
            print('Anna')


if __name__ == '__main__':
    main()
