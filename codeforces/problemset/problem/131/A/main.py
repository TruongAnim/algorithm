# https://codeforces.com/problemset/problem/131/A

def main():
    s = input()
    check = s.isupper() or (s[1:].isupper() and s[0].islower()) or (len(s) == 1 and s[0].islower())
    if check:
        for i in s:
            if i.isupper():
                print(i.lower(), end='')
            else:
                print(i.upper(), end='')
    else:
        print(s)


if __name__ == '__main__':
    main()
