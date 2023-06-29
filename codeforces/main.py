# https://app.codesignal.com/arcade/code-arcade/labyrinth-of-nested-loops/W5Sq7taLSzNHh8GiF
# Crossword Formation

import string


def get_indices(string, c):
    indices = [i for i in range(len(string)) if string[i] == c]
    return indices


_w = []
_maps = []


def solution(words):
    _w.extend(words)
    letters = string.ascii_lowercase
    for i in words:
        temp = {}
        for j in letters:
            temp[j] = get_indices(i, j)
        _maps.append(temp)
    permutations = permute(words)
    return sum(count_solutions(p) for p in permutations if p[0] < p[1]) * 2


def find_indices(string, c):
    index = _w.index(string)
    return _maps[index][c]


def count_solutions(words):
    count = 0
    for i in range(len(words[0])):
        for j in find_indices(words[1], words[0][i]):
            for k in range(i + 2, len(words[0])):
                for l in find_indices(words[2], words[0][k]):
                    for m in range(j + 2, len(words[1])):
                        if m - j + l >= len(words[2]):
                            continue
                        for n in find_indices(words[3], words[1][m]):
                            if (k - i + n < len(words[3]) and
                                    words[3][k - i + n] == words[2][m - j + l]):
                                count += 1
    return count


permArr = []
usedWords = []


def permute(input):
    for i in range(len(input)):
        w = input.pop(i)
        usedWords.append(w)
        if len(input) == 0:
            permArr.append(tuple(i for i in usedWords))
        permute(input)
        input.insert(i, w)
        usedWords.pop()
    return permArr
