# https://codeforces.com/contest/1899/problem/B

def get_divider(n):
    result = []
    for i in range(2, int(n / 2) + 1):
        if n % i == 0:
            result.append(i)
    return result


def get_sum(a):
    current = 0
    result = []
    for i in a:
        current += i
        result.append(current)
    return result


def split_into_subarrays(arr, n):
    avg_length = len(arr) // n
    remaining = len(arr) % n
    subarrays = [arr[i * avg_length + min(i, remaining):(i + 1) * avg_length + min(i + 1, remaining)] for i in range(n)]
    return subarrays


def brute_force(a):
    result = max(a) - min(a)
    for i in range(2, len(a)):
        if len(a) % i == 0:
            temp = split_into_subarrays(a, i)
            s = list(map(sum, temp))
            result = max(max(s) - min(s), result)
    print(result)


def main():
    # import sys
    # sys.stdin = open('input.txt', 'r')
    test = int(input())
    for t in range(test):
        n = int(input())
        a = list(map(int, input().split(' ')))
        # brute_force(a)
        # continue
        d = get_divider(n)
        s = get_sum(a)
        result = max(a) - min(a)
        for i in d:
            _max = 0
            _min = 10 ** 20
            for j in range(int(n / i)):
                index2 = i * (j + 1) - 1
                index1 = i * j - 1
                temp2 = s[index2]
                temp1 = 0 if index1 < 0 else s[index1]
                temp = temp2 - temp1
                _max = max(temp, _max)
                _min = min(temp, _min)
            diff = _max - _min
            result = max(result, diff)
        print(result)


if __name__ == '__main__':
    main()
