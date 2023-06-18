# https://codeforces.com/contest/1834/problem/A

def main():
    testcase = int(input())
    for _ in range(testcase):
        n = int(input())
        a = map(int, input().split(' '))
        positive = 0
        negative = 0
        for i in a:
            if i < 0:
                negative += 1
            else:
                positive += 1
        need = 0
        if negative > positive:
            need = (negative - positive)
            if need % 2 == 0:
                need = need // 2
            else:
                need = (need // 2) + 1
            negative -= need
            positive += need
        if negative % 2 == 1:
            need += 1
        print(need)


if __name__ == '__main__':
    main()
