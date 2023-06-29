# https://codeforces.com/contest/1845/problem/C

def main():
    test = int(input())
    for _ in range(test):
        s = input()
        s = tuple(int(i) for i in s)
        # print(s)
        m = int(input())
        l = input()
        r = input()
        index = 0
        oke = False
        for i in range(m):
            d = int(l[i])
            u = int(r[i])
            t = []

            for j in range(d, u + 1):
                temp = get_index(s, j, index)
                t.append(temp)
                if temp == -1:
                    oke = True
                    break
            if oke:
                break
            else:
                index = max(t)+1
        if oke:
            print('YES')
        else:
            print('NO')


def get_index(s, j, start):
    # print('find', j, 'in', start)
    try:
        index = s.index(j, start)
        return index
    except ValueError:
        return -1


if __name__ == '__main__':
    main()
