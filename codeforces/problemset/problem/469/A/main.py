def main():
    n = int(input())
    line1 = list(map(int, input().split(' ')))
    line2 = list(map(int, input().split(' ')))
    total = set(line1[1:] + line2[1:])
    if len(total) >= n:
        print('I become the guy.')
    else:
        print('Oh, my keyboard!')


if __name__ == '__main__':
    main()
