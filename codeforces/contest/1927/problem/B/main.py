# https://codeforces.com/contest/1927/problem/B

def main():
    import sys
    sys.stdin = open('input.txt', 'r')
    test = int(input())
    for _ in range(test):
        alpha = [chr(i) for i in range(ord('a'), ord('z') + 1)]
        n = int(input())
        count = [0 for i in range(n + 1)]
        a = map(int, input().split(' '))
        s = ''
        for i in a:
            c = count[i]
            count[i] += 1
            s += alpha[c]
        print(s)


if __name__ == '__main__':
    main()
