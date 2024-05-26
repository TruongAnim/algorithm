# https://codeforces.com/contest/1977/problem/B


found = False


def recursion(A, r, index, l):
    global found
    if found:
        return
    if index == 0:
        if l == 0:
            oke = True
            for i in range(len(r) - 1):
                if r[i] != 0 and r[i + 1] != 0:
                    oke = False
            if oke:
                found = list(r)
        return
    if l == 0:
        recursion(A, r, index - 1, 0)
        return
    if r[index] == 0:
        r[index - 1] = -1
        recursion(A, r, index - 1, l - A[index - 1])
        r[index - 1] = 1
        recursion(A, r, index - 1, l + A[index - 1])
    r[index - 1] = 0
    recursion(A, r, index - 1, l)


def main():
    import sys
    sys.stdin = open('input.txt', 'r')
    test = int(input())
    A = [2 ** i for i in range(32)]
    for _ in range(test):
        l = int(input())
        # print('l = ', l)
        global found
        found = False
        for index, i in enumerate(A):
            if l == i:
                found = [0 for i in range(index)] + [1]
                break
            elif i > l:
                recursion(A, [0 for i in range(index)] + [1], index, A[index] - l)
                recursion(A, [0 for i in range(index - 1)] + [1], index - 1, A[index - 1] - l)
                break
        print(len(found))
        print(' '.join(map(str, found)))


if __name__ == '__main__':
    main()
