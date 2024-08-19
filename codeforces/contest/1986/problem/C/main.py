# https://codeforces.com/contest/1986/problem/C

def main():
    import sys
    sys.stdin = open('input.txt', 'r')
    test = int(input())
    for _ in range(test):
        n, m = map(int, input().split(' '))
        a = [*input()]
        ind = sorted(map(int, input().split(' ')))
        c = sorted(input())
        # print(ind)
        # print(c)
        # print(a)
        pre = -1
        index = 0
        for i in range(len(ind)):
            if ind[i] == pre:
                index - 1
                continue
            pre = ind[i]
            a[ind[i] - 1] = c[index]
            index += 1
        print(''.join(a))


if __name__ == '__main__':
    main()
