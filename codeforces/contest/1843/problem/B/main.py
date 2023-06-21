# https://codeforces.com/contest/1843/problem/B

def main():
    tesecase = int(input())
    for _ in range(tesecase):
        n = int(input())
        a = tuple(i for i in map(int, input().split(' ')) if i != 0)
        b = []
        if len(a) == 0:
            print(0, 0)
            continue
        sign = True if a[0] > 0 else False
        for i in range(1, len(a)):
            temp = True if a[i] > 0 else False
            if sign != temp:
                b.append(sign)
                sign = temp
        b.append(sign)
        negative = 0
        for i in b:
            if not i:
                negative += 1
        print(sum([abs(i) for i in a]), negative)


if __name__ == '__main__':
    main()
