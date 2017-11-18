# Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
#
# For example:
# Given the below binary tree and sum = 22,
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1
# return
# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]

# 解法同112

class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

class PathSumII(object):
    def solution1(self, root, n):
        if not root:
            return []
        result = []
        self.recursive(root, n, 0, result, [])
        return result

    def recursive(self, root, n, sum, result, temp):
        if not root:
            return
        total = sum + root.val
        temp.append(root.val)
        if total > n:
            return
        elif total == n:
            result.append(temp[:len(temp)])
            return
        self.recursive(root.left, n, total, result, temp)
        temp.pop()
        self.recursive(root.right, n, total, result, temp)
        temp.pop()