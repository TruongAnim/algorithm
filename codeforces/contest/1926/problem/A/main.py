# https://codeforces.com/contest/1926/problem/A

def main():
    test = int(input())
    M = {}
    for i in range(26):
        for j in range(26):
            for k in range(26):
                ii = chr(ord('a') + i)
                jj = chr(ord('a') + j)
                kk = chr(ord('a') + k)
                if (i + j + k + 3) not in M.keys():
                    M[i + j + k + 3] = ii + jj + kk
    for _ in range(test):
        n = int(input())
        print(M[n])


if __name__ == '__main__':
    main()
