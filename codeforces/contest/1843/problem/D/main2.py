# https://codeforces.com/contest/1843/problem/C

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.leaf = 1
        self.isTravel = False
        self.children = []

    def add_child(self, child):
        self.children.append(child)


def preorder_traversal(root):
    stack = [root]
    while stack:
        current_node = stack.pop()
        current_node.isTravel = True
        current_node.children = [i for i in current_node.children if not i.isTravel]

        for child in current_node.children:
            stack.append(child)


def calculate_node_value(root):
    stack = [root]

    while stack:
        current_node = stack[-1]
        is_leaf = True

        for child in current_node.children:
            if child.isTravel:
                stack.append(child)
                is_leaf = False

        if is_leaf:
            current_node.isTravel = False
            descendant_sum = sum(child.leaf for child in current_node.children)
            current_node.leaf = descendant_sum if current_node.children else 1
            stack.pop()


def main():
    tesecase = int(input())
    for _ in range(tesecase):
        n = int(input())
        m = {u: TreeNode(u) for u in range(1, n + 1)}

        for i in range(n - 1):
            u, v = map(int, input().split(' '))
            m[u].add_child(m[v])
            m[v].add_child(m[u])

        preorder_traversal(m[1])
        calculate_node_value(m[1])
        q = int(input())
        for i in range(q):
            x, y = map(int, input().split(' '))
            print(m[x].leaf * m[y].leaf)


if __name__ == '__main__':
    main()
