def main():
    import sys
    sys.stdin = open('input.txt', 'r')
    lines = []
    for i in range(5):
        lines.append(input().split(' '))
    for i in range(5):
        for j in range(5):
            if lines[i][j] == '1':
                print(abs(2 - i) + abs(2 - j))
                return


if __name__ == '__main__':
    main()
