import sys


def main():
    start = 1
    end = 1000000
    while (True):
        # print(start, end)
        if start == end:
            print('! {0}'.format(start))
            sys.stdout.flush()
            return
        test = (start + end + 1) // 2
        result = check(test)
        if result == -1:
            end = test - 1
        else:
            start = test


def check(n):
    print(n)
    sys.stdout.flush()
    result = input()
    if result == '<':
        return -1
    else:
        return 1


if __name__ == '__main__':
    main()
