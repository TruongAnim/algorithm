# https://codeforces.com/problemset/problem/443/A

def main():
    sett = input()[1:-1].replace(' ', '').split(',')
    print(sett)
    sett = set(i for i in sett if len(i) > 0)
    print(len(sett))


if __name__ == "__main__":
    main()
