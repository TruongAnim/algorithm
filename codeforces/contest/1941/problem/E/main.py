# https://codeforces.com/contest/1941/problem/E

import heapq


class MinHeap:
    def __init__(self):
        self.heap = []

    def add_number(self, num):
        heapq.heappush(self.heap, num)

    def remove_number(self, num):
        self.heap.remove(num)
        heapq.heapify(self.heap)

    def get_min_element(self):
        return self.heap[0]

    heapq


def get_min(a, m, d):
    b = [1 for i in range(m)]
    heap = MinHeap()
    heap.add_number(1)
    for i in range(1, m):
        pre = i - d - 2
        if pre >= 0:
            heap.remove_number(b[pre])
        b[i] = heap.get_min_element() + a[i] + 1
        heap.add_number(b[i])
    return b[-1]


def main():
    test = int(input())
    for _ in range(test):
        n, m, k, d = map(int, input().split(' '))
        a = []
        for i in range(n):
            temp = list(map(int, input().split(' ')))
            a.append(get_min(temp, m, d))
        result = sum(a[:k])
        pre = result
        for i in range(k, n):
            pre += a[i]
            pre -= a[i-k]
            result = min(result, pre)
        print(result)


if __name__ == '__main__':
    main()
