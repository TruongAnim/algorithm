# https://codeforces.com/problemset/problem/1343/A

def main():
    s = []
    sum = 0
    for i in range(30):
        sum += 2 ** i
        s.append(sum)
    test = int(input())
    for _ in range(test):
        n = int(input())
        for i in s[1:]:
            if n % i == 0:
                print(n // i)
                break


if __name__ == '__main__':
    main()
