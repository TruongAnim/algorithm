def main():
    n, t = map(int, input().split(' '))
    queue = [x for x in input()]
    while (t):
        t -= 1
        temp = queue.copy()
        for index, item in enumerate(queue[:-1]):
            if queue[index] == 'B' and queue[index + 1] == 'G':
                temp[index] = 'G'
                temp[index + 1] = 'B'
        queue = temp
    print(''.join(queue))


if __name__ == '__main__':
    main()
