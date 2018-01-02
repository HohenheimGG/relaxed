# coding: utf-8
# Print a binary tree in an m*n 2D string array following these rules:
#
# 1. The row number m should be equal to the height of the given binary tree.
# 2. The column number n should always be an odd number.
# 3. The root node’s value (in string format) should be put in the exactly middle of the first row it can be put.
# 4. The column and the row where the root node belongs will separate the rest space into two parts (left-bottom part and right-bottom part).
# 5. You should print the left subtree in the left-bottom part and print the right subtree in the right-bottom part.
# 6. The left-bottom part and the right-bottom part should have the same size.
# 7. Even if one subtree is none while the other is not,
# you don’t need to print anything for the none subtree but still need to leave the space as large as that for the other subtree.

# However, if two subtrees are none, then you don’t need to leave space for both of them.
# Each unused space should contain an empty string “”.
# Print the subtrees following the same rules.

# Example 1:
# Input:
#      1
#     /
#    2
# Output:
# [["", "1", ""],
#  ["2", "", ""]]
# Example 2:
# Input:
#      1
#     / \
#    2   3
#     \
#      4
# Output:
# [["", "", "", "1", "", "", ""],
#  ["", "2", "", "", "", "3", ""],
#  ["", "", "4", "", "", "", ""]]
# Example 3:
# Input:
#       1
#      / \
#     2   5
#    /
#   3
#  /
# 4
# Output:
#
# [["",  "",  "", "",  "", "", "", "1", "",  "",  "",  "",  "", "", ""]
#  ["",  "",  "", "2", "", "", "", "",  "",  "",  "",  "5", "", "", ""]
#  ["",  "3", "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]
#  ["4", "",  "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]]
# Note: The height of binary tree is in the range of [1, 10].

import math


class Tree(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class PrintBinaryTree(object):
    def solution1(self, root):
        if not root:
            return None
        height = self.find_depth(root)

        nums = []
        size = math.pow(2, height) - 1
        for i in range(0, size):
            nums.append([])
            for j in range(0, height):
                nums[i][j] = ''

        self.sub_print(nums, root, 0, size, 1, height)
        return nums

    def find_depth(self, root):
        if not root:
            return 0
        left = self.find_depth(root.left)
        right = self.find_depth(root.right)
        return max(left, right) + 1

    def sub_print(self, nums, root, left, right, cur, max_height):
        if cur > max_height or not root or left > right:
            return None
        mid = math.ceil((left + right) / 2)
        nums[cur][mid] = root.val
        self.sub_print(nums, root.left, left, mid - 1, cur + 1, max_height)
        self.sub_print(nums, root.right, mid + 1, right, cur + 1, max_height)
        return nums
