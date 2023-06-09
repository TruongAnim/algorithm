# https://codeforces.com/problemset/problem/344/A

def main():
    n = int(input())
    sum = 1
    pre = input()
    for i in range(n - 1):
        magnet = input()
        if pre[-1] == magnet[0]:
            sum += 1
        pre = magnet
    print(sum)


if __name__ == '__main__':
    main()
