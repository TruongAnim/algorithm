# https://codeforces.com/problemset/problem/118/A

def main():
    raw = input()
    result = ''
    for i in raw:
        if i in ["A", "O", "Y", "E", "U", "I", "a", "o", "y", "e", "u", "i", ]:
            continue
        result += '.' + i
    print(result.lower())


if __name__ == '__main__':
    main()
