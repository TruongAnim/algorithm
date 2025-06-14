# https://codeforces.com/problemset/problem/1829/A

def main():
    t = int(input())
    for _ in range(t):
        s = input()
        raw = 'codeforces'
        result = 0
        for i, j in zip(s, raw):
            if i != j:
                result += 1
        print(result)


if __name__ == '__main__':
    main()
