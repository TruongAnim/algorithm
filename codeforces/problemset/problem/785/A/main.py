# https://codeforces.com/problemset/problem/785/A

def main():
    n = int(input())
    result = 0
    for i in range(n):
        result += get_faces(input())
    print(result)


def get_faces(s):
    if s == 'Tetrahedron':
        return 4
    if s == 'Cube':
        return 6
    if s == 'Octahedron':
        return 8
    if s == 'Icosahedron':
        return 20
    if s == 'Dodecahedron':
        return 12


if __name__ == '__main__':
    main()
