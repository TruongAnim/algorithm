# https://codeforces.com/problemset/problem/58/A

def main():
    word = input()
    expect = 'hello'
    for i in expect:
        f = word.find(i)
        if f < 0:
            print('NO')
            return
        else:
            word = word[f + 1:]
    print('YES')


if __name__ == '__main__':
    main()
