def main():
    import sys
    sys.stdin = open('input.txt', 'r')
    math_input = input().split('+')
    math_input.sort()
    for i in math_input[:-1]:
        print(i + '+', end='')
    print(math_input[-1])


if __name__ == '__main__':
    main()
