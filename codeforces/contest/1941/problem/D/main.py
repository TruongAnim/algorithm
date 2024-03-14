# https://codeforces.com/contest/1941/problem/D

def thow_ball(a, n, p, c):
    temp = set()
    for i in a:
        index1 = (i + p) % n
        if index1 == 0:
            index1 = n
        index2 = (i - p)
        if index2 <= 0:
            index2 = n + index2
        # print(i, p, index2)
        if c == '0':
            temp.add(index1)
        elif c == '1':
            temp.add(index2)
        else:
            temp.add(index1)
            temp.add(index2)
    return temp


def main():
    import sys
    sys.stdin = open('input.txt', 'r')
    test = int(input())
    for _ in range(test):
        n, m, x = map(int, input().split(' '))
        a = {x, }
        for i in range(m):
            temp = input().split(' ')
            p = int(temp[0])
            c = temp[1]
            a = thow_ball(a, n, p, c)
        print(len(a))
        temp = sorted(a)
        for i in temp:
            print(i, end=' ')
        print()


if __name__ == '__main__':
    main()
