# https://codeforces.com/contest/1899/problem/C

def max_subarray_sum(arr):
    max_sum = float('-inf')
    current_sum = 0
    start = 0
    end = 0
    s = 0

    for i, num in enumerate(arr):
        current_sum += num

        if current_sum > max_sum:
            max_sum = current_sum
            start = s
            end = i

        if current_sum < 0:
            current_sum = 0
            s = i + 1

    return arr[start:end + 1]


def is_same_party(a, b):
    return a % 2 != b % 2


def get_subarray(a, n):
    sub = [a[0]]
    result = max(a)
    for i in range(1, n):
        if is_same_party(a[i], a[i - 1]):
            sub.append(a[i])
        else:
            # print(sub)
            result = max(sum(max_subarray_sum(sub)), result)
            sub.clear()
            sub.append(a[i])
    if len(sub) > 1:
        # print(sub)
        result = max(sum(max_subarray_sum(sub)), result)
    return result


def main():
    import sys
    sys.stdin = open('input.txt', 'r')
    test = int(input())
    for t in range(test):
        n = int(input())
        a = list(map(int, input().split(' ')))
        print(get_subarray(a, n))


if __name__ == '__main__':
    main()
