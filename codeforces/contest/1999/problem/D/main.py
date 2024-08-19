# https://codeforces.com/contest/1999/problem/D
import random
import string


def generate_strings(length):
    if length <= 0:
        return ("", "")

    # String 1: contains lowercase letters and '?' with the given length
    chars1 = string.ascii_lowercase + '?'
    string1 = ''.join(random.choice(chars1) for _ in range(length))

    # String 2: contains only lowercase letters with length <= given length
    length2 = random.randint(1, length)  # length of string 2
    string2 = ''.join(random.choice(string.ascii_lowercase) for _ in range(length2))

    return string1, string2


def main():
    import sys
    sys.stdin = open('input.txt', 'r')
    test = int(input())
    for _ in range(test):
        # s, t = generate_strings(random.randint(1,10))
        s = input()
        t = input()
        start = 0
        oke = False
        result = []
        for i in range(len(t)):
            for j in range(start, len(s)):
                if s[j] == t[i] or s[j] == '?':
                    result.append(t[i])
                    i += 1
                    start = j + 1
                    if i == len(t):
                        oke = True
                    break
                else:
                    result.append(s[j])
                    j += 1
                    start = j
            if start >= len(s):
                break
        # print(s)
        # print(t)
        print('YES' if oke else 'NO')
        if oke:
            temp = len(result)
            for i in range(temp, len(s)):
                result.append(s[i] if s[i] != '?' else 'a')
            print(''.join(result))


if __name__ == '__main__':
    main()
