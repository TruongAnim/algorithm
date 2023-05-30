def main():
    n = input()
    colors = input()
    pre = colors[0]
    count = 1
    result = []
    for i in colors[1:]:
        print(pre, i)
        if i != pre:
            result.append(count)
            pre = i
            count = 1
        else:
            count += 1

    result.append(count)
    sum = 0
    for i in result:
        if i > 1:
            sum+=i-1
    print(sum)


if __name__ == '__main__':
    main()
