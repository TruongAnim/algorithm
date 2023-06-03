def main():
    n = input()
    result = input()
    a, d = 0, 0
    for i in result:
        if i == 'A':
            a += 1
        else:
            d += 1
    if a > d:
        print('Anton')
    elif a < d:
        print('Danik')
    else:
        print('Friendship')


if __name__ == '__main__':
    main()
