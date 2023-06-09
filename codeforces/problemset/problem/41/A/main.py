# https://codeforces.com/problemset/problem/41/A

def main():
    word1 = input()
    word2 = input()
    if word1 == word2[::-1]:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()
