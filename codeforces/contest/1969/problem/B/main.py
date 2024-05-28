# https://codeforces.com/contest/1969/problem/B

def main():
    import sys
    sys.stdin = open('input.txt', 'r')
    test = int(input())
    for _ in range(test):
        s = input()
        start = -1
        end = -1
        for index, i in enumerate(s):
            if i == '1':
                if start == -1:
                    start = end = index
                else:
                    end = index
            if start != -1 and i == '0':
                break
        result = 0
        if start == end == -1:
            print(0)
            continue
        # print(start, end)
        while True:
            if end >= len(s) - 1:
                break
            result += end - start + 2
            end += 1
            start += 1
            # print('1', start, end)
            for i in range(end + 1, len(s)):
                if s[i] == '1':
                    end += 1
                else:
                    break
            # print('2', start, end)

        print(result)


if __name__ == '__main__':
    main()
