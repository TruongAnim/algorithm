# https://codeforces.com/contest/1948/problem/B

def is_non_decreasing(number):
    num_str = str(number)

    for i in range(len(num_str) - 1):
        if num_str[i] > num_str[i + 1]:
            return False
    return True


def check(A):
    is_oke = True
    for i in range(len(A) - 1):
        if A[i] > A[i + 1]:
            is_oke = False
            break
    return is_oke


def process(A):
    B = []
    for i in range(len(A) - 1):
        if A[i] > A[i + 1] and A[i] >= 10:
            B.append(A[i] // 10)
            B.append(A[i] % 10)
        else:
            B.append(A[i])
    B.append(A[-1])
    return B


def main():
    import sys
    sys.stdin = open('input.txt', 'r')
    test = int(input())
    for _ in range(test):
        n = int(input())
        A = list(map(int, input().split(' ')))
        for i in range(55):
            A = process(A)
        # print(A)
        is_oke = check(A)
        if is_oke:
            print('YES')
        else:
            print('NO')


if __name__ == '__main__':
    main()
