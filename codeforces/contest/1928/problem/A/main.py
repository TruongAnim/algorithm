# https://codeforces.com/contest/1928/problem/A

def main():
    test = int(input())
    for _ in range(test):
        a, b = map(int, input().split(' '))
        _min = min(a, b)
        _max = max(a, b)
        if _min % 2 == 0:
            new_max = _max * 2
            new_min = _min // 2
            if _min != new_min and _max != new_max:
                print('YES')
                continue
        if _max % 2 == 0:
            new_max = _max // 2
            new_min = _min * 2
            if _min != new_max and _max != new_min:
                print('YES')
                continue
        print('NO')


if __name__ == '__main__':
    main()
