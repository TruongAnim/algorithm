# https://codeforces.com/contest/1841/problem/A

def main():
    testcase = int(input())
    for test in range(testcase):
        process()


result = 0


def process():
    global result
    result = 0
    n = int(input())
    A = {1: n}
    recursion(A, 0)
    if result == 1:
        print('Alice')
    else:
        print('Bob')


def recursion(A, t):
    # print(A)
    check = True
    for k in A.keys():
        if A[k] > 1:
            check = False
    if check and t % 2 == 0:
        global result
        result = 1

    for k in A.keys():
        value = A[k]
        for i in range(2, value + 1):
            B = A.copy()
            B[k] -= i
            if k * i in B.keys():
                B[k * i] += 1
            else:
                B[k * i] = 1
            recursion(B, t + 1)


if __name__ == '__main__':
    main()
