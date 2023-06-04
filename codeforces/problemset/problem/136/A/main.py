def main():
    n = int(input())
    l = list(map(int, input().split(' ')))
    new_l = l.copy()
    for index, item in enumerate(l):
        new_l[item - 1] = index + 1
    new_l = list(map(str, new_l))
    print(' '.join(new_l))


if __name__ == '__main__':
    main()
