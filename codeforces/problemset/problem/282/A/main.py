def main():
    import sys
    sys.stdin = open('input.txt', 'r')
    n = int(input())
    value = 0
    for i in range(n):
        statement = input()
        if '+' in statement:
            value+=1
        else:
            value-=1
    print(value)

if __name__ == '__main__':
    main()
