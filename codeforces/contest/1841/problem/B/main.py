# https://codeforces.com/contest/1841/problem/B

def main():
    testcase = int(input())
    for test in range(testcase):
        process()


def process():
    n = int(input())
    A = list(map(int, input().split(' ')))
    B = [A[0]]
    print(1, end='')
    increase = True
    for i in A[1:]:
        if increase:
            if i >= B[-1]:
                B.append(i)
                print(1, end='')
            elif i <= B[0]:
                B.append(i)
                print(1, end='')
                increase = False
            else:
                print(0, end='')
        else:
            if B[-1] <= i <= B[0]:
                B.append(i)
                print(1, end='')
            else:
                print(0, end='')
    print()


if __name__ == '__main__':
    main()
