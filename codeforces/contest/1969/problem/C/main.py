# https://codeforces.com/contest/1969/problem/C

def can_reduce(a, b):
    if a[0] < b[0]:
        return 1, (b[0] - a[0]) * b[1], a, b
    if a[0] > b[0]:
        return -1, (a[0] - b[0]) * a[1], a, b
    return 0, 0


def main():
    import sys
    sys.stdin = open('input.txt', 'r')
    test = int(input())
    h = []
    for _ in range(test):
        n, k = map(int, input().split(' '))
        A = list([i, 1] for i in map(int, input().split(' ')))
        sum1 = sum(i[0] for i in A)
        result = 0
        for i in range(k):
            B = []
            _max = (0, 0)
            for i in range(n - 1):
                temp = can_reduce(A[i], A[i + 1])
                B.append(temp)
                if _max[1] < temp[1]:
                    _max = temp
            print(_max)
            result += _max[1]
            if _max[0] == -1:
                _max[2][0] = _max[3][0]
                _max[3][1] += _max[2][1]
            elif _max[0] == 1:
                _max[3][0] = _max[2][0]
                _max[2][1] += _max[3][1]
        print(A)
        print(sum1 - result)
        h.append(sum1-result)
    return h


def check(A, turn, k, gb_sum):
    if turn >= k:
        gb_sum[0] = min(gb_sum[0], sum(A))
        # print(gb_sum, A)
        return
    for i in range(0, len(A)):
        temp = A[i]
        if i == 0:
            A[i] = min(A[i], A[i + 1])
        elif i == len(A)-1:
            A[i] = min(A[i], A[i - 1])
        else:
            A[i] =  min(A[i], A[i-1], A[i+1])
        check(A, turn + 1, k, gb_sum)
        A[i] = temp


def test_solution():
    # import sys
    # sys.stdin = open('input.txt', 'r')
    test = int(input())
    h = []
    for _ in range(test):
        n, k = map(int, input().split(' '))
        A = list(i for i in map(int, input().split(' ')))
        if n == 1:
            print(sum(A))
            h.append(sum(A))
            continue
        gb_sum = [sum(A)]
        check(A, 0, k, gb_sum)
        print(gb_sum[0])
        h.append(gb_sum[0])
    return h


if __name__ == '__main__':
    a = test_solution()
    # b = main()
    # print(a)
    # print(b)
