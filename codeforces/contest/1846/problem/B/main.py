# https://codeforces.com/contest/1846/problem/B

def main():
    test = int(input())
    for _ in range(test):
        r = []
        r.append(input())
        r.append(input())
        r.append(input())
        c0 = [r[0][0], r[1][0], r[2][0]]
        c1 = [r[0][1], r[1][1], r[2][1]]
        c2 = [r[0][2], r[1][2], r[2][2]]

        d1 = [r[0][0], r[1][1], r[2][2]]
        d2 = [r[0][2], r[1][1], r[2][0]]
        result = [check(r[0]), check(r[1]), check(r[2]), check(c0), check(c1), check(c2), check(d1), check(d2)]
        oke = False
        for i in result:
            if len(i) > 0 and i != '.':
                print(i)
                oke = True
                break
        if not oke:
            print('DRAW')


def check(a):
    if a[0] == a[1] == a[2]:
        return a[0]
    else:
        return ''


if __name__ == '__main__':
    main()
