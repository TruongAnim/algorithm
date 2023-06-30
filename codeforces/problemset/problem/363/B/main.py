# https://codeforces.com/problemset/problem/363/B

def main():
    n, k = map(int, input().split(' '))
    f = tuple(map(int, input().split(' ')))
    s = sum(f[:k])
    _min = s
    _index = 1
    for i in range(k, len(f)):
        s += f[i]
        s -= f[i - k]
        if s < _min:
            _min = s
            _index = i - k + 2
    print(_index)


if __name__ == '__main__':
    main()
