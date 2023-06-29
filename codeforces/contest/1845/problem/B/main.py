# https://codeforces.com/contest/1845/problem/B

class P:
    def __init__(self, a):
        self.x = a[0]
        self.y = a[1]


def main():
    test = int(input())
    for _ in range(test):
        a = P(tuple(map(int, input().split())))
        b = P(tuple(map(int, input().split())))
        c = P(tuple(map(int, input().split())))
        rectangle1 = {'left': min(a.x, b.x), 'top': max(a.y, b.y), 'right': max(a.x, b.x), 'bottom': min(a.y, b.y)}
        rectangle2 = {'left': min(a.x, c.x), 'top': max(a.y, c.y), 'right': max(a.x, c.x), 'bottom': min(a.y, c.y)}
        top = min(rectangle1['top'], rectangle2['top'])
        bottom = max(rectangle1['bottom'], rectangle2['bottom'])
        left = max(rectangle1['left'], rectangle2['left'])
        right = min(rectangle1['right'], rectangle2['right'])
        if top >= bottom and left <= right:
            print((top - bottom + 1) + (right - left + 1) - 1)


if __name__ == '__main__':
    main()
