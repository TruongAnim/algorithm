# https://codeforces.com/problemset/problem/268/A

def main():
    n = int(input())
    H, G = [], []
    for i in range(n):
        h, g = map(int, input().split(' '))
        H.append(h)
        G.append(g)
    result = 0
    for i in range(n):
        for j in range(n):
            if i != j and H[i] == G[j]:
                result += 1
    print(result)


if __name__ == '__main__':
    main()
