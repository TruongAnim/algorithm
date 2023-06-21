# https://codeforces.com/contest/1843/problem/C

class TreeNode:
    def __init__(self, value):
        self.value = value
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
    node_values = {root: root.value}  # Store the value of each node

    while stack:
        current_node = stack[-1]
        is_leaf = True

        for child in current_node.children:
            if child not in node_values:
                stack.append(child)
                is_leaf = False

        if is_leaf:
            descendant_sum = sum(node_values[child] for child in current_node.children)
            node_values[current_node] = descendant_sum if current_node.children else 1
            stack.pop()

    return node_values


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
        result = calculate_node_value(m[1])
        q = int(input())
        for i in range(q):
            x, y = map(int, input().split(' '))
            print(result[m[x]] * result[m[y]])


if __name__ == '__main__':
    main()
