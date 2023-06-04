def main():
    n = int(input())
    l = map(int, input().split(' '))
    for i in l:
        if i == 1:
            print('HARD')
            return
    print('EASY')


if __name__=='__main__':
    main()