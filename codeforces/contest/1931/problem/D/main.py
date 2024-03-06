# https://codeforces.com/contest/1931/problem/D
# Time limit

def calculate(a, x, y):
    b1 = [i % x for i in a]
    b2 = [i % y for i in a]
    sorted_arrays = zip(*sorted(zip(b1, b2)))
    # Unpack the sorted arrays
    b1, b2 = map(list, sorted_arrays)
    result = 0
    index = len(b1) - 1
    print(b1, b2)
    for i in range(len(a)):
        need_sum = (x - b1[i]) % x
        need_sub = b2[i] % y
        print(need_sum, need_sub)

        while True:
            print('index', index)
            if b1[index] < need_sum or index < 0:
                break
            if b1[index] == need_sum and b2[index] == need_sub:
                result += 1
                print('result++', result)
            index -= 1
    print(result)


def check_result(a, x, y):
    # a = sorted(a)
    _sum = set()
    _sub = set()
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if (a[i] + a[j]) % x == 0:
                _sum.add((i, j))
            if (a[i] - a[j]) % y == 0:
                _sub.add((i, j))
    print(_sum)
    print(_sub)
    print(len(_sum.intersection(_sub)))


def main():
    import sys
    sys.stdin = open('input.txt', 'r')
    test = int(input())
    for t in range(test):
        n, x, y = map(int, input().split(' '))
        a = list(map(int, input().split(' ')))
        # calculate(a, x, y)
        check_result(a, x, y)


if __name__ == '__main__':
    main()
