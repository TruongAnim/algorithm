# https://codeforces.com/problemset/problem/1352/A

def main():
    t = int(input())
    for _ in range(t):
        n = input()
        count = 0
        l = []
        for i, v in enumerate(n):
            if v != '0':
                count += 1
                l.append(int(v) * 10 ** (len(n) - i - 1))
        print(count)
        print(' '.join(str(i) for i in l))


if __name__ == '__main__':
    main()
