# https://codeforces.com/problemset/problem/4/A

def main():
    a = int(input())
    if a > 2 and a % 2 == 0:
        print("YES")
    else:
        print("NO")


# Check if this file is being run directly (not imported)
if __name__ == "__main__":
    main()
