# https://codeforces.com/contest/1969/problem/A

def main():
    test = int(input())
    for _ in range(test):
        n = int(input())
        A = list(map(int, input().split(' ')))
        A.insert(0, 0)
        check = False
        # print(A)
        for index, i in enumerate(A):
            if index != 0 and index == A[i]:
                check = True
        if check:
            print(2)
        else:
            print(3)


if __name__ == '__main__':
    main()
