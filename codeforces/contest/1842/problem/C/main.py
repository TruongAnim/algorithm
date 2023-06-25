# https://codeforces.com/contest/1842/problem/C

def main():
    testcase = int(input())
    for _ in range(testcase):
        n = int(input())
        a = tuple(map(int, input().split(' ')))
        b = [0] * n
        c = [0] * n
        first_index = {}
        for i, item in enumerate(a):
            if item in first_index:
                first_index[item].append(i)
            else:
                first_index[item] = [i]
        for i in first_index:
            first_index[i] = first_index[i][::-1]
        for i in range(1, len(a)):
            index = first_index[a[i]]
            _max = b[i - 1]
            j = index[-1]
            if j < i:
                temp1 = (i - j + (b[j] if c[j] else b[j] + 1))
                temp2 = (i - j + 1) + b[j - 1] if j > 0 else 0
                _max = max(_max, temp1, temp2)
                c[i] = 1
                index.pop()
            b[i] = _max
        print(b[-1])


if __name__ == '__main__':
    main()
