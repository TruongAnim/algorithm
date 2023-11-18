# https://codeforces.com/contest/1857/problem/D


def main():
    test = int(input())
    for _ in range(test):
        n = int(input())
        a = list(map(int, input().split(' ')))
        b = list(map(int, input().split(' ')))
        d = list(a[i] - b[i] for i in range(n))
        _max = max(d)
        s = find_indices_of_value(d, _max)
        print(len(s))
        print(' '.join(map(str, s)))


def find_indices_of_value(arr, k):
    indices = []
    for i in range(len(arr)):
        if arr[i] == k:
            indices.append(i + 1)
    return indices


if __name__ == '__main__':
    main()
