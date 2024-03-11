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
        a = []
        a.append(input())
        a.append(input())
        m = []
        count = 0
        result = '5'
        for i in range(n):
            s = a[0][:i + 1] + a[1][i:]
            c = compare_strings(s, result)
            # print(s, result, c)
            if c == 0:
                count += 1
                print('i', i)
            if c < 0:
                result = s
                count = 1

        print(result)
        print(count)


if __name__ == '__main__':
    main()
