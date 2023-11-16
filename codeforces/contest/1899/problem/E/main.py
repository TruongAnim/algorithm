# https://codeforces.com/contest/1899/problem/E

def first_smallest_index(arr):
    if not arr:
        return None  # Return None for empty arrays

    min_value = float('inf')
    min_index = None

    for i, num in enumerate(arr):
        if num < min_value:
            min_value = num
            min_index = i

    return min_index


def is_non_decreasing(arr):
    n = len(arr)
    for i in range(1, n):
        if arr[i] < arr[i - 1]:
            return False
    return True


def main():
    import sys
    sys.stdin = open('input.txt', 'r')
    test = int(input())
    for t in range(test):
        n = int(input())
        a = list(map(int, input().split(' ')))
        _min = min(a)
        index_min = first_smallest_index(a)
        if is_non_decreasing(a[index_min + 1:]):
            print(index_min)
        else:
            print(-1)


if __name__ == '__main__':
    main()
