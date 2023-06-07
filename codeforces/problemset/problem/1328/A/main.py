def main():
    testcase = int(input())
    for test in range(testcase):
        a, b = map(int, input().split(' '))
        if a % b == 0:
            print(0)
        else:
            print((a // b + 1) * b - a)


if __name__ == '__main__':
    main()
