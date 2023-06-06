price = [2 ** i for i in range(32)]

sum = 0


def main():
    import sys
    sys.stdin = open('input.txt', 'r')
    testcase = int(input())
    for _ in range(testcase):
        n, k = map(int, input().split(' '))
        if k > 15:
            k = 15
        process(n, k)


def process(n, k):
    global sum
    sum = 0
    printSubsequences(price[:k], 0, [], n)
    print(sum + 1)


def printSubsequences(arr, index, subarr, n):
    if index == len(arr):
        if len(subarr) != 0:
            total = 0
            for i in subarr:
                total += i
            if total <= n:
                global sum
                sum += 1
    else:
        printSubsequences(arr, index + 1, subarr, n)
        printSubsequences(arr, index + 1,
                          subarr + [arr[index]], n)
    return


if __name__ == '__main__':
    main()
