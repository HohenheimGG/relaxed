# Given a binary tree, flatten it to a linked list in-place.
#
# For example,
# Given
#
#          1
#         / \
#        2   5
#       / \   \
#      3   4   6
# The flattened tree should look like:
#    1
#     \
#      2
#       \
#        3
#         \
#          4
#           \
#            5
#             \
#              6

class Tree:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

class FlattenBinaryTreeToLinkedList:
    def __init__(self):
        self.prev = None

    def solution1(self, root):
        if not root:
            return None

    def recursive(self, root):
        if root is None:
            return
        self.recursive(root.right)
        self.recursive(root.left)
        root.right = self.prev
        root.left = None
        prev = root

if __name__ == '__main__':
    pass