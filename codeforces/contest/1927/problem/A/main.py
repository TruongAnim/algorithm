# https://codeforces.com/contest/1927/problem/A

def main():
    test = int(input())
    for _ in range(test):
        n = int(input())
        s = input()
        start = -1
        end = -1
        for index, i in enumerate(s):
            if i == 'B':
                start = index
        for index, i in enumerate(s[::-1]):
            if i == 'B':
                end = len(s) - index - 1
        if start == -1 or end == -1:
            print(0)
        else:
            print(start - end + 1)


if __name__ == '__main__':
    main()
