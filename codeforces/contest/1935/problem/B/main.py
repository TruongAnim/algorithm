# https://codeforces.com/contest/1935/problem/B


def main():
    test = int(input())
    for _ in range(test):
        n = int(input())
        a = list(map(int, input().split(' ')))
        b = [False for i in range(n)]
        missing = n
        for i in a:
            b[i] = True
        for i, value in enumerate(b):
            if not value:
                missing = min(i, missing)
        # print(missing)
        if missing == 0:
            print(2)
            print(1, 1)
            print(2, n)
            continue
        temp = [False for i in range(missing)]
        count = 0
        left = 0
        result = []
        for i, v in enumerate(a):
            if v < missing and not temp[v]:
                temp[v] = True
                count += 1
                if count == missing:
                    if len(result) == 1:
                        result.append((left, n - 1))
                        break
                    result.append((left, i))
                    left = i + 1
                    count = 0
                    temp = [False for i in range(missing)]
        if len(result) < 2:
            print(-1)
        else:
            print(2)
            for i in result:
                print(i[0] + 1, i[1] + 1)


if __name__ == '__main__':
    main()