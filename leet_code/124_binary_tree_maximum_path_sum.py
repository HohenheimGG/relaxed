# Given a binary tree, find the maximum path sum.
#
# For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree
# along the parent-child connections.
#
# The path must contain at least one node and does not need to go through the root.
#
# For example:
# Given the below binary tree,
#
#        1
#       / \
#      2   3
# Return 6.

# 求最大路径和就等于下面三个值的最大值：
# 左子树的最大路径和
# 右子树最大路径和
# 左子树单路 + 右子树单路 + root.val

import sys

class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

class BinaryTreePathSum(object):
    def solution1(self, root):
        if not root:
            return 0
        result, _ = self.recursive(root)
        return result

    def recursive(self, node):
        if not node:
            return -sys.maxint, 0
        left = self.recursive(node.left)
        right = self.recursive(node.right)
        singPath = max(left[1] + node.val, right[1] + node.val, 0)
        maxPath = max(left[0], right[0], left[1] + right[1] + node.val)
        return maxPath, singPath

