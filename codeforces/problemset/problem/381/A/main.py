# https://codeforces.com/problemset/problem/381/A

def main():
    n = int(input())
    s = tuple(map(int, input().split(' ')))
    sereja, dima = 0, 0
    i, j = 0, len(s) - 1
    turn = 0
    while i <= j:
        larger = 0
        if s[i] > s[j]:
            larger = s[i]
            i += 1
        else:
            larger = s[j]
            j -= 1
        if turn % 2 == 0:
            sereja += larger
        else:
            dima += larger
        turn += 1
    print(sereja, dima)


if __name__ == '__main__':
    main()
