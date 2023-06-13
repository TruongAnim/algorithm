# https://codeforces.com/problemset/problem/427/A

def main():
    n = int(input())
    a = list(map(int, input().split(' ')))
    police = 0
    untreat = 0
    for i in a:
        if i == -1:
            if police > 0:
                police -= 1
            else:
                untreat += 1
        else:
            police += i
    print(untreat)


if __name__ == '__main__':
    main()
