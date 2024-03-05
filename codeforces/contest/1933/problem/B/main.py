# https://codeforces.com/contest/1933/problem/B

def main():
    test = int(input())
    for _ in range(test):
        n = int(input())
        a = list(map(int, input().split(' ')))
        is_contain_one = False
        for i in a:
            if i % 3 == 1:
                is_contain_one = True

        s = sum(a)
        # print('sum', s)
        if s % 3 == 0:
            print(0)
        elif s % 3 == 2:
            print(1)
        else:
            if n == 1:
                print(1)
            elif is_contain_one:
                print(1)
            else:
                print(2)


if __name__ == '__main__':
    main()
