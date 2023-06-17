# https://codeforces.com/problemset/problem/1409/A

def main():
    testcase = int(input())
    for _ in range(testcase):
        process()


def process():
    aa, bb = map(int, input().split(' '))
    a = min(aa, bb)
    b = max(aa, bb)
    result = (b - a) // 10
    result += 1 if b != (a + result * 10) else 0
    print(result)


if __name__ == '__main__':
    main()
