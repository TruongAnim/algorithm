# https://codeforces.com/contest/1853/problem/A

def main():
    test = int(input())
    for _ in range(test):
        n = int(input())
        a = list(map(int, input().split(' ')))
        min_diff = 10**10
        for i in range(n-1):
            if a[i] > a[i+1]:
                min_diff = -1
                break
            else:
                min_diff = min(min_diff, a[i+1]-a[i])
        if min_diff == -1:
            print(0)
        elif min_diff == 0:
            print(1)
        else:
            print(min_diff//2+1)


if __name__ == '__main__':
    main()
