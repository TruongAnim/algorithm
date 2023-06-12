# https://codeforces.com/problemset/problem/337/A

def main():
    student, puzzle = map(int, input().split(' '))
    A = sorted(list(map(int, input().split(' '))))
    diff = 10 ** 10
    for i in range(0, len(A) - student + 1):
        new_diff = A[i + student - 1] - A[i]
        if diff > new_diff:
            diff = new_diff
    print(diff)


if __name__ == '__main__':
    main()
