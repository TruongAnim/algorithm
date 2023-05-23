def main():
    import sys
    sys.stdin = open('input.txt', 'r')
    n, k = map(int, input().split())
    sum = 0
    min_score = 0
    scores = [int(i) for i in input().split()]
    for i in range(n):
        score = scores[i]
        if i < k and score > 0:
            sum += 1
            min_score = score
        else:
            if score == min_score and min_score > 0:
                sum += 1
    print(sum)


if __name__ == '__main__':
    main()
