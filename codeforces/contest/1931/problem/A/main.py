# https://codeforces.com/contest/1931/problem/A

def main():
    test = int(input())
    for _ in range(test):
        s = int(input())
        a = list(map(int, input().split(' ')))
        count_a = 0
        for i in range(s):
            if a[i] == 1:
                a = a[i:]
                break
        for i in range(len(a)):
            if a[i] == 1:
                count_a += 1
        a = a[::-1]
        result = 0
        while True:
            for i in range(len(a)):
                if a[i] == 1:
                    for j in range(i + 1, len(a)):
                        if a[j] == 0:
                            a[i] = 0
                            a[j] = 1
                            result += 1
            find_a = False
            is_oke = True
            for i in range(len(a)):
                if find_a and a[i] == 1 and a[i - 1] == 0:
                    is_oke = False
                if a[i] == 1:
                    find_a = True
            if is_oke:
                break
        print(result)


if __name__ == '__main__':
    main()
