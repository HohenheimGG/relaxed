# Given a binary tree, return the zigzag level order traversal of its nodes' values.
# (ie, from left to right, then right to left for the next level and alternate between).
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its zigzag level order traversal as:
# [
#   [3],
#   [20,9],
#   [15,7]
# ]


class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class ZigzagLevelOrder(object):
    def solution1(self, root):
        if not root:
            return []
        result = []
        self.travel(root, result, 0)
        return result

    def travel(self, root, result, level):
        if not root:
            return
        if len(result) < level + 1:
            result.append([])

        if level % 2 == 0:
            result[level].append(root.val)
        else:
            result[level].insert(0, root.val)

        self.travel(root.left, result, level + 1)
        self.travel(root.right, result, level + 1)

    def solution2(self, root):
        result = []
        if not root:
            return result

        queue = []
        level = 0
        queue.append(root)
        while len(queue) != 0:
            result.append([])
            size = len(queue)
            for index in range(0, size):
                item = queue[index]
                if level % 2 == 0:
                    result[level].append(item.val)
                else:
                    result[level].insert(0, item.val)
                if item.left:
                    queue.append(item.left)
                if item.right:
                    queue.append(item.right)
            queue = queue[size:len(queue)]
            level += 1
        return result


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node6 = ListNode(6)
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

    result = ZigzagLevelOrder().solution2(node1)
    print result
