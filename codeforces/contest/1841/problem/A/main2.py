# https://codeforces.com/contest/1841/problem/A

def main():
    testcase = int(input())
    for test in range(testcase):
        process()


def process():
    n = int(input())
    if n <= 4:
        print('Bob')
    else:
        print('Alice')


if __name__ == '__main__':
    main()
