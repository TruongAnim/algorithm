def main():
    n = int(input())
    l = list(map(int, input().split(' ')))
    sum = 0
    for i in l:
        sum += i
    print(sum / len(l))


if __name__ == '__main__':
    main()
