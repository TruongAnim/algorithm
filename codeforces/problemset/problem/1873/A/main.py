# https://codeforces.com/problemset/problem/1873/A

def main():
    test = int(input())
    for _ in range(test):
        s = input()
        # If already "abc" or can be made "abc" with one swap
        if (s == "abc" or 
            s == "bac" or  # swap 'b' and 'a'
            s == "cba" or  # swap 'c' and 'a'
            s == "acb"):   # swap 'c' and 'b'
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    main()