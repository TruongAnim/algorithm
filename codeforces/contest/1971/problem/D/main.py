# https://codeforces.com/contest/1971/problem/D

def compress_binary(binary_str):
    compressed_str = ""
    prev_digit = None

    for digit in binary_str:
        if digit != prev_digit:
            compressed_str += digit
            prev_digit = digit

    return compressed_str


def main():
    import sys
    sys.stdin = open('input.txt', 'r')
    test = int(input())
    for _ in range(test):
        s = input()
        s = compress_binary(s)

        if s == '01':
            print(1)
        elif len(s) == 1:
            print(1)
        elif len(s) == 2:
            print(2)
        else:
            print(len(s) - 1)


if __name__ == '__main__':
    main()
