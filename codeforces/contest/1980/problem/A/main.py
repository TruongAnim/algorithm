# https://codeforces.com/contest/1980/problem/A

def main():
    test = int(input())
    for _ in range(test):
        n, m = map(int, input().split(' '))
        A = input()
        bank = {}
        for i in A:
            if i not in bank:
                bank[i] = 0
            bank[i] += 1
        problems = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        result = 0
        for i in problems:
            if i not in bank:
                result += m
            elif bank[i] < m:
                result += m - bank[i]
        print(result)


if __name__ == '__main__':
    main()
