# https://codeforces.com/problemset/problem/155/A

def main():
    n = int(input())
    a = list(map(int, input().split(' ')))
    _min = a[0]
    _max = a[0]
    result = 0
    for i in a[1:]:
        if i < _min:
            _min = i
            result += 1
        if i > _max:
            _max = i
            result += 1
    print(result)


if __name__ == '__main__':
    main()
