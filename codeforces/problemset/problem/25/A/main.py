# https://codeforces.com/problemset/problem/25/A

def main():
    n = input()
    s = list(map(int, input().split(' ')))
    even = 0
    odd = 0
    i_even = 0
    i_odd = 0
    for i in range(len(s)):
        if s[i] % 2 == 0:
            even += 1
            i_even = i + 1
        else:
            odd += 1
            i_odd = i + 1
    if even < odd:
        print(i_even)
    else:
        print(i_odd)


if __name__ == '__main__':
    main()
