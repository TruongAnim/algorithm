# https://codeforces.com/contest/1984/problem/B

def main():
    import sys
    sys.stdin = open('input.txt', 'r')
    test = int(input())
    for _ in range(test):
        n = input()[::-1]
        p1, p2 = '', ''
        du = 0
        for i in range(len(n)-1):
            num = int(n[i]) - du
            if num < 0 or num > 8:
                du = 10
                break
            if num % 2 == 0:
                num += 10
                need = num // 2
                # print("need 1", need)
                p1 += str(need)
                p2 += str(need)
            else:
                num += 10
                need = num // 2
                # print("need 2", need)
                p1 += str(need)
                p2 += str(need + 1)
            du = 1
        if du == int(n[-1]):
            print('YES')
        else:
            print('NO')
        # print(p1, p2)


if __name__ == '__main__':
    main()
