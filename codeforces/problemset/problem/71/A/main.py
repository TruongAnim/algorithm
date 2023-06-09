# https://codeforces.com/problemset/problem/71/A

def process(word):
    if len(word) <= 10:
        print(word)
    else:
        print(word[0] + str(len(word) - 2) + word[-1])


def main():
    import sys
    sys.stdin = open('input.txt', 'r')
    # sys.stdout = open('output.txt', 'w')

    n = int(input())
    for i in range(n):
        process(input())


# Check if this file is being run directly (not imported)
if __name__ == "__main__":
    main()
