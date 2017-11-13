# You need to find the largest value in each row of a binary tree.
#
# Example:
# Input:
#
#           1
#          / \
#         3   2
#        / \   \
#       5   3   9
#
# Output: [1, 3, 9]

class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

class FindLargestValue(object):
    def solution1(self, root):
        temp = []
        result = []
        if not root:
            return result
        temp.append(root)
        size = len(temp)
        while True:
            if size == 0:
                break
            max = temp[0].val
            for index in range(0, size):
                item = temp[index]
                if not item:
                    continue
                if item.left:
                    temp.append(item.left)
                if item.right:
                    temp.append(item.right)
                if max < item.val:
                    max = item.val
            result.append(max)
            if len(temp) == size:
                break
            temp = temp[size:len(temp)]
            size = len(temp)
        return result

if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(3)
    node3 = ListNode(2)
    node4 = ListNode(5)
    node5 = ListNode(3)
    node6 = ListNode(9)

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.right = node6
    result = FindLargestValue().solution1(node1)
    print result
