# https://codeforces.com/problemset/problem/43/A

def main():
    n = int(input())
    _map = {}
    for i in range(n):
        s = input()
        if s not in _map:
            _map[s] = 1
        else:
            _map[s] += 1
    print(max(_map, key=_map.get))


if __name__ == '__main__':
    main()
