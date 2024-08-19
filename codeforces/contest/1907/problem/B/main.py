# https://codeforces.com/contest/1907/problem/B

def main():
    # import sys
    # sys.stdin = open('lv10.csv', 'r')
    test = int(input())
    for t in range(test):
        s = input()
        temp = []
        il = 0
        ul = 0
        for i in s[::-1]:
            if i == 'B':
                ul += 1
            elif i == 'b':
                il += 1
            elif i.isupper():
                if ul > 0:
                    ul -= 1
                else:
                    temp.append(i)
            elif i.islower():
                if il > 0:
                    il -= 1
                else:
                    temp.append(i)
        print(''.join(temp[::-1]))


if __name__ == '__main__':
    main()