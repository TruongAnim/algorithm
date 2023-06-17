# https://codeforces.com/contest/1840/problem/A

def main():
    import sys
    sys.stdin = open('input.txt', 'r')
    testcase = int(input())
    for _ in range(testcase):
        n = int(input())
        encrypt = input()
        result = ''
        pre = ''
        for i in encrypt:
            if pre == '':
                pre = i
                result += i
            elif pre == i:
                pre = ''
        print(result)


if __name__ == "__main__":
    main()
