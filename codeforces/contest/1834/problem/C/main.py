# https://codeforces.com/contest/1834/problem/C

def main():
    testcase = int(input())
    for _ in range(testcase):
        n = int(input())
        s = input()
        t = input()
        xuoi = 0
        nguoc = 0
        for i, j in zip(s, t):
            if i != j:
                xuoi += 1
        for i, j in zip(s, t[::-1]):
            if i != j:
                nguoc += 1
        result = min(get_xuoi(xuoi), get_nguoc(nguoc))
        # print(xuoi, nguoc)
        print(result)


def get_xuoi(xuoi):
    if xuoi == 0:
        return 0
    elif xuoi == 1:
        return 1
    elif xuoi % 2 == 0:
        return 2 * xuoi
    else:
        return 2 * xuoi - 1


def get_nguoc(nguoc):
    if nguoc <= 1:
        return 2
    if nguoc % 2 == 0:
        return 2 * nguoc - 1
    else:
        return 2 * nguoc


if __name__ == '__main__':
    main()
