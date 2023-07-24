# https://codeforces.com/problemset/problem/489/C
# not resolve

def main():
    m, s = map(int, input().split(' '))
    _min = find_min(m, s)
    _max = find_max(m, s)

    print(_min, _max)


def find_min(length, sum_of_digits):
    if sum_of_digits == 0:
        return -1
    if sum_of_digits > 9 * length:
        return -1  # No solution possible

    number = [1] * length  # Initialize the number with all zeros

    remain = length - 1
    for i in range(length):
        if sum_of_digits - (remain) >= 9:
            number[i] = 9
            sum_of_digits -= 9
        else:
            number[i] = sum_of_digits - (remain)
            sum_of_digits -= sum_of_digits - (remain)
        remain -= 1

    num = ''.join(map(str, number))
    print(num)
    reverse = int(num[::-1]) if num[0] != '0' else 10 ** 100
    return min(int(num), reverse)


def find_max(length, sum_of_digits):
    if sum_of_digits > 9 * length:
        return -1  # No solution possible

    number = [0] * length  # Initialize the number with all zeros

    for i in range(length - 1, -1, -1):
        if sum_of_digits >= 9:
            number[i] = 9
            sum_of_digits -= 9
        else:
            number[i] = sum_of_digits
            sum_of_digits = 0

    return int(''.join(map(str, number)))


if __name__ == '__main__':
    main()
