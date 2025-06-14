# https://codeforces.com/problemset/problem/514/A

def main():
    n = input()
    result = ''
    for i in n:
        num_i = int(i)
        if num_i > 4:
            result += str(9 - num_i)
        else:
            result += i
    if result[0] == '0':
        print(9, end='')
        print(result[1:])
    else:
        print(result)


if __name__ == '__main__':
    main()
