# Two elements of a binary search tree (BST) are swapped by mistake.
#
# Recover the tree without changing its structure.
#
# Note:
# A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?


class Tree:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


class RecoverBinarySearchTree:
    def __init__(self):
        self.result = []

    def solution1(self, root):
        if not root:
            return []
        self.recursive(root)

        temp = None
        result = self.result
        index = 1
        if result[0].val > result[1].val:
            temp = result[0]
        while index < len(result) - 1:
            if result[index - 1].val < result[index].val < result[index + 1].val:
                continue
            if not temp:
                temp = result[index]
            else:
                temp.val ^= result[index].val
                result[index].val ^= temp.val
                temp.val ^= result[index].val
                break

    def recursive(self, root):
        if not root:
            return
        left = root.left
        right = root.right
        self.recursive(left)
        self.result.append(root)
        self.recursive(right)

if __name__ == '__main__':
    pass
