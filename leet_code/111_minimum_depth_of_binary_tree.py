# Given a binary tree, find its minimum depth.
#
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

class Tree:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class MinimumDepth:
    def solution1(self, root):
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        if not root.left:
            return self.solution1(root.right) + 1
        if not root.right:
            return self.solution1(root.left) + 1
        return min(self.solution1(root.left), self.solution1(root.right)) + 1

if __name__ == '__main__':
    root = Tree(0)
    root.left = Tree(1)
    root.left.left = Tree(3)
    root.left.right = Tree(4)
    root.right = Tree(2)
    root.right.left = Tree(5)
    result = MinimumDepth().solution1(root)
    print result
