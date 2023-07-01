def main():
    import sys
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')
    n = int(input())
    for i in range(n):
        a = input().upper()
        print(a)


if __name__ == '__main__':
    main()
