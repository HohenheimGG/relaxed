# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
#
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
#
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# But the following [1,2,2,null,3,null,3] is not:
#     1
#    / \
#   2   2
#    \   \
#    3    3
# Note:
# Bonus points if you could solve it both recursively and iteratively.

class Tree:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class SymmetricTree:
    def solution1(self, root):
        return not root or self.recursive(root.left, root.right)

    def recursive(self, left, right):
        if not left or right:
            return left == right
        if left.val != right.val:
            return False
        return self.recursive(left.left, right.right) and self.recursive(left.right, right.left)

if __name__ == '__main__':
    pass
