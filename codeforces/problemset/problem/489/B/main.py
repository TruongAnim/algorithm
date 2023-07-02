# https://codeforces.com/problemset/problem/489/B

def main():
    a = int(input())
    la = sorted(map(int, input().split(' ')))
    b = int(input())
    lb = map(int, input().split(' '))
    _map = {}
    for i in lb:
        if i in _map:
            _map[i] += 1
        else:
            _map[i] = 1
    count = 0
    for i in la:
        options = (i - 1, i, i + 1)
        for j in options:
            if j in _map and _map[j] > 0:
                count += 1
                _map[j] -= 1
                break
    print(count)


if __name__ == '__main__':
    main()
