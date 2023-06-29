# https://codeforces.com/contest/1845/problem/C

def is_subarray(arr, subarr):
    index = 0
    for i in subarr:
        try:
            index = arr.index(i, index)
            index+=1

        except ValueError:
            return False
    return True


def generate_strings(a, b):
    if len(a) != len(b):
        return []

    results = []
    generate_strings_recursive(a, b, "", 0, results)
    return results


def generate_strings_recursive(a, b, current_str, index, results):
    if index == len(a):
        results.append(current_str)
        return

    for char_code in range(ord(a[index]), ord(b[index]) + 1):
        char = chr(char_code)
        generate_strings_recursive(a, b, current_str + char, index + 1, results)


def main():
    test = int(input())
    for _ in range(test):
        s = input()
        s = tuple(int(i) for i in s)
        # print(s)
        m = int(input())
        l = input()
        r = input()
        all = generate_strings(l, r)
        for a in all:
            t = tuple(int(i) for i in a)
            if not is_subarray(s, t):
                print(t)
                break
        else:
            print('no')



def get_index(s, j, start):
    # print('find', j, 'in', start)
    try:
        index = s.index(j, start)
        return index
    except ValueError:
        return -1


if __name__ == '__main__':
    main()
