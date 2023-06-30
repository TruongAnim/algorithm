# https://codeforces.com/problemset/problem/1472/B

def main():
    test = int(input())
    for _ in range(test):
        n = int(input())
        w1, w2 = 0, 0
        w = map(int, input().split(' '))
        for i in w:
            if i == 1:
                w1 += 1
            else:
                w2 += 1
        total = w1 + w2 * 2
        if w1 > 0 and total % 2 == 0:
            print('YES')
        elif w1 == 0 and w2 % 2 == 0:
            print('YES')
        else:
            print('NO')


if __name__ == '__main__':
    main()
