# https://codeforces.com/contest/1847/problem/B

def main():
    test = int(input())
    for _ in range(test):
        result = ''
        for i in range(8):
            a = input()
            result = result + get_char(a)
        print(result)


def get_char(a):
    for i in a:
        if i != '.':
            return i
    return ''


if __name__ == '__main__':
    main()
