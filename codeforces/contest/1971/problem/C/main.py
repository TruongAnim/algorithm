# https://codeforces.com/contest/1971/problem/C

def on_segment(p, q, r):
    if q[0] <= max(p[0], r[0]) and q[0] >= min(p[0], r[0]) and \
            q[1] <= max(p[1], r[1]) and q[1] >= min(p[1], r[1]):
        return True
    return False


def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0  # Collinear
    return 1 if val > 0 else 2  # Clockwise or Counterclockwise


def intersect(A, B, C, D):
    o1 = orientation(A, B, C)
    o2 = orientation(A, B, D)
    o3 = orientation(C, D, A)
    o4 = orientation(C, D, B)

    if o1 != o2 and o3 != o4:
        return True

    if o1 == 0 and on_segment(A, C, B):
        return True
    if o2 == 0 and on_segment(A, D, B):
        return True
    if o3 == 0 and on_segment(C, A, D):
        return True
    if o4 == 0 and on_segment(C, B, D):
        return True

    return False


def main():
    import sys
    sys.stdin = open('input.txt', 'r')
    test = int(input())
    A = [(0, 0), (5, 8.66), (8.66, 5), (10, 0), (8.66, -5), (5, - 8.66), (0, -10), (-5, - 8.66), (-8.66, -5), (-10, 0),
         (-8.66, 5), (-5, 8.66), (0, 10)]
    for _ in range(test):
        a, b, c, d = map(int, input().split(' '))
        # print(a, b, c, d)
        _a = A[a]
        _b = A[b]
        _c = A[c]
        _d = A[d]
        # print(_a, _b, _c, _d)
        if intersect(_a, _b, _c, _d):
            print('YES')
        else:
            print('NO')


if __name__ == '__main__':
    main()
