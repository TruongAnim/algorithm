# https://codeforces.com/problemset/problem/141/A

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    M = {}
    for i in s1 + s2:
        if i in M.keys():
            M[i] += 1
        else:
            M[i] = 1
    M3 = {}
    for i in s3:
        if i in M3.keys():
            M3[i] += 1
        else:
            M3[i] = 1
    if M.keys() != M3.keys():
        print('NO')
        return
    for i in M.keys():
        if M[i] != M3[i]:
            print('NO')
            return
    print('YES')


if __name__ == '__main__':
    main()
