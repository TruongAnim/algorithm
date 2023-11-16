# https://codeforces.com/contest/1899/problem/A

def main():
    test = int(input())
    for i in range(test):
        a = int(input())
        if a%3 == 0:
            print('Second')
        else:
            print('First')

if __name__ == '__main__':
    main()
