# https://codeforces.com/contest/1976/problem/A

def check(s):
    numbers = []
    alpha = []
    is_number = True
    for i in s:
        if i.isalpha():
            is_number = False
        if is_number:
            numbers.append(i)
        else:
            alpha.append(i)
    print(numbers, alpha)
    for i in numbers:
        if not i.isdigit():
            return False
    for i in alpha:
        if not i.isalpha():
            return False
    if numbers != sorted(numbers):
        return False
    if alpha != sorted(alpha):
        return False
    return True


def main():
    import sys
    sys.stdin = open('input.txt', 'r')
    test = int(input())
    for _ in range(test):
        n = int(input())
        s = input()
        if check(s):
            print('YES')
        else:
            print('NO')


if __name__ == '__main__':
    main()
