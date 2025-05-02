# https://codeforces.com/contest/2009/problem/B


def main():
    test = int(input())
    for _ in range(test):
        n = int(input())
        A = []
        result = []
        for i in range(n):
            s = input()
            A.append(s)
        for i in A[::-1]:
            for index,j in enumerate(i):
                if j == '#':
                    result.append(str(index+1))
        print(' '.join(result))

if __name__ == '__main__':
    main()
