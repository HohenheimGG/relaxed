# Given a binary tree and a sum, determine
# if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
#
# For example:
# Given the below binary tree and sum = 22,
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \      \
#         7    2      1
# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.


class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

class PathSum(object):
    def solution1(self, root, sum):
        result = []
        temp = []
        if not root:
            return result
        self.recursive(root, temp, result, 0, sum)
        return result

    def recursive(self, root, temp, result, num, sum):
        if not root:
            return
        total = num + root.val
        temp.append(root.val)
        if total > sum:
            return
        elif total < sum:
            self.recursive(root.left, temp, result, total, sum)
            temp.pop()
            self.recursive(root.right, temp, result, total, sum)
            temp.pop()
        else:
            result.append(temp[:len(temp)])

if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(3)
    node5 = ListNode(5)
    node6 = ListNode(2)
    node7 = ListNode(7)
    node8 = ListNode(8)
    node9 = ListNode(9)
    node10 = ListNode(10)

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7
    node4.left = node8
    node4.right = node9
    node5.left = node10
    result = PathSum().solution1(node1, 6)
    print result
