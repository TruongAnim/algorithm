# https://codeforces.com/problemset/problem/279/B

import random


def generate_random_data():
    n = random.randint(1, 10 ** 5)
    t = random.randint(1, 10 ** 4)
    a = [random.randint(1, 10 ** 2) for _ in range(n)]
    return n, t, a


def brute_force(n, k, A):
    result = 0
    for i in range(0, n):
        s = 0
        for j in range(i, n):
            s += A[j]
            if s <= k:
                result = max(result, j - i + 1)
            else:
                break
    return result


def solution(n, k, A):
    e, sum, result = 0, 0, 0
    for i in range(0, n):
        e = max(e, i)
        for j in range(e, n):
            # print(i, j, result)
            e = j
            if sum + A[j] <= k:
                sum += A[j]
                result = max(result, j - i + 1)
            else:
                break
        sum -= A[i]
        sum = max(0, sum)
        # print(sum)
    return result


def main():
    n, k = map(int, input().split(' '))
    A = list(map(int, input().split(' ')))
    print(solution(n, k, A))
    return
    for i in range(100000):
        n, k, A = generate_random_data()
        s = solution(n, k, A)
        b = brute_force(n, k, A)
        if s != b:
            print(n, k)
            print(A)
            print(s, b)


if __name__ == "__main__":
    main()
