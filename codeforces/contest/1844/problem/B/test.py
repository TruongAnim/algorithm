# https://codeforces.com/contest/1844/problem/B

def main():
    testcase = int(input())
    for _ in range(testcase):
        n = int(input())
        arr = []
        for i in range(2, n + 1, 2):
            print(i, end=' ')
            arr.append(i)
        arr.append(1)
        print(1, end=' ')
        temp = [i for i in range(3, n + 1, 2)]
        for i in temp[::-1]:
            print(i, end=' ')
            arr.append(i)
        print(arr)
        count = 0
        for t in get_subarrays(arr):
            if is_prime(find_missing_positive_integer(t)):
                count += 1
        print('=>', count)
        print()

        permutations = get_permutations(n)
        _max = 0
        for perm in permutations:
            count = 0
            for t in get_subarrays(perm):
                if is_prime(find_missing_positive_integer(t)):
                    count += 1
            _max = max(_max, count)
        p = 1
        for perm in permutations:
            count = 0
            for t in get_subarrays(perm):
                if is_prime(find_missing_positive_integer(t)):
                    count += 1
            if count == _max and p > 0:
                print(perm, count)
                p -= 1;
        print(p)


def get_subarrays(arr):
    subarrays = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr) + 1):
            subarrays.append(arr[i:j])
    return subarrays


def find_missing_positive_integer(arr):
    n = len(arr)

    # Separate positive and non-positive numbers
    positive_nums = [num for num in arr if num > 0]

    # Sort positive numbers
    positive_nums.sort()

    # Find the smallest missing positive integer
    smallest_missing = 1
    for num in positive_nums:
        if num == smallest_missing:
            smallest_missing += 1
        else:
            return smallest_missing

    return smallest_missing


def is_prime(number):
    if number <= 1:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True


from itertools import permutations


def get_permutations(n):
    arr = list(range(1, n + 1))
    perms = list(permutations(arr))
    return perms


if __name__ == '__main__':
    main()
