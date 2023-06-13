# https://codeforces.com/problemset/problem/4/C

def main():
    n = int(input())
    mapp = {}
    for i in (range(n)):
        name = input()
        if mapp.get(name) is not None:
            print('{0}{1}'.format(name, mapp[name]))
            mapp[name] += 1
        else:
            print('OK')
            mapp[name] = 1


if __name__ == '__main__':
    main()
