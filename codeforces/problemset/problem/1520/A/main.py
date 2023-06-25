# https://codeforces.com/problemset/problem/1520/A

def main():
    testcase = int(input())
    for _ in range(testcase):
        n = int(input())
        s = input()
        _map = {s[0]: 1}
        for i in range(1, len(s)):
            if s[i - 1] != s[i]:
                if s[i] in _map:
                    print('NO')
                    break
                else:
                    _map[s[i]] = 1
        else:
            print('YES')


if __name__ == '__main__':
    main()
