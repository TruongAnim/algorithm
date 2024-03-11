# https://codeforces.com/contest/1937/problem/B

def compare_strings(str1, str2):
    if str1 < str2:
        return -1
    elif str1 > str2:
        return 1
    else:
        return 0


def main():
    import sys
    sys.stdin = open('input.txt', 'r')
    test = int(input())
    for _ in range(test):
        n = int(input())
        a = [input(), input()]
        m = []
        count = 0
        result = a[0][0]
        is_done = False
        for i in range(n - 1):
            right = a[0][i + 1]
            bot = a[1][i]
            if right == bot:
                result += right
                count += 1
            elif right > bot:
                result += a[1][i:]
                is_done = True
                break
            else:
                result += right
                count = 0
        if not is_done:
            result += a[1][-1]
        print(result)
        print(count + 1)


if __name__ == '__main__':
    main()
