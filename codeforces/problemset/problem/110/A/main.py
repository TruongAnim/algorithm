# https://codeforces.com/problemset/problem/110/A

def main():
    number = input()
    l_number = 0
    for i in number:
        if i == '4' or i == '7':
            l_number+=1
    if l_number == 4 or l_number == 7:
        print('YES')
    else:
        print('NO')


if __name__=='__main__':
    main()