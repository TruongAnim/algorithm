price = [2 ** i for i in range(33)]


def main():
    import sys
    sys.stdin = open('input.txt', 'r')
    testcase = int(input())
    for _ in range(testcase):
        n, k = map(int, input().split(' '))
        print(process(n, k) + 1)


def process(n, k):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if k == 0:
        return 0
    if k == 1:
        return 1
    if n == 2 and k == 2:
        return 2
    if n > 2 and k == 2:
        return 3
    if n == 2 and k > 2:
        return 2
    if k > 32:
        k = 32
    if n >= price[k] - 1:
        return price[k] - 1;

    index = 0
    for i, p in enumerate(price[:k]):
        if n > p:
            index = i
    return (2 ** (index) - 1) + process(n - price[index] + 1, index + 1)


if __name__ == "__main__":
    # print(price)
    main()
