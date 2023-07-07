# https://codeforces.com/contest/1845/problem/A

def main():
    test = int(input())
    for _ in range(test):
        n, m, h = map(int, input().split(' '))
        a = []
        for i in range(n):
            a.append(tuple(sorted(map(int, input().split(' ')))))
        r = get_point(a[0], h)
        result = 1
        for i in a[1:]:
            temp = get_point(i, h)
            if temp[0] > r[0] or (temp[0] == r[0] and temp[1] < r[1]):
                result += 1
        print(result)


def get_point(a, h):
    _sum = 0
    total_time = 0
    remain = h
    current_time = 0
    for i in a:
        if remain >= i:
            _sum += 1
            current_time += i
            total_time += current_time
            remain -= i
    return _sum, total_time


if __name__ == '__main__':
    main()
