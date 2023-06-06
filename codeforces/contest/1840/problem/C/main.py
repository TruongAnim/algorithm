def main():
    import sys
    sys.stdin = open('input.txt', 'r')
    testcase = int(input())
    for _ in range(testcase):
        process()


def process():
    n, k, q = map(int, input().split(' '))
    temps = list(map(int, input().split(' ')))
    temps.append(1 * 10 ** 10)
    sum = 0
    result = 0
    for i in temps:
        if i <= q:
            sum += 1
        else:
            result += calculate(k, sum)
            sum = 0
    print(result)


def calculate(k, sum):
    if sum < k:
        return 0
    if sum == k:
        return 1
    return total(sum - k + 1)


def total(n):
    return n * (n + 1) // 2


if __name__ == "__main__":
    main()
    # print(calculate(3, 3))
