# {1,2,3}
# => {3,1,2}, {3,2,1}, {1,2,3}, {1,3,2} , {2,1,3}, {2,3,1}.

def main():
    inputArray = [i for i in range(3)]
    print(permutation(inputArray))


def permutation(lst):
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [lst]
    l = []
    for i in range(len(lst)):
        m = lst[i]
        remLst = lst[:i] + lst[i + 1:]
        for p in permutation(remLst):
            l.append([m] + p)
    return l


if __name__ == '__main__':
    main()
