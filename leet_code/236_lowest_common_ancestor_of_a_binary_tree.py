# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
#
# According to the definition of LCA on Wikipedia:
# The lowest common ancestor is defined between two nodes
# v and w as the lowest node in T that has both v and w as descendants
# (where we allow a node to be a descendant of itself).
#
#         _______3______
#        /              \
#     ___5__          ___1__
#    /      \        /      \
#    6      _2       0       8
#          /  \
#          7   4
# For example, the lowest common ancestor (LCA) of nodes 5 and 1 is 3.
# Another example is LCA of nodes 5 and 4 is 5,
# since a node can be a descendant of itself according to the LCA definition.


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

class LowestCommon(object):
    def solution1(self, root, vnode, wnode):
        if not root or not vnode or not wnode:
            return None
        return self.recursive(root, vnode, wnode)

    def recursive(self, root, vnode, wnode):
        if not root or root.val == vnode.val or root.val == wnode.val:
            return root
        right = self.recursive(root.right, vnode, wnode)
        left = self.recursive(root.left, vnode, wnode)
        if right and left:
            return root
        return left if not right else right

    def solution2(self, root, vnode, wnode):
        vstack, wstack = self.findPath(root, vnode), self.findPath(root, wnode)
        vlen, wlen = len(vstack), len(wstack)
        target, x, minLen = None, 0, min(vlen, wlen)
        while x < minLen and vstack[x] == wstack[x]:
            target, x = vstack[x], x + 1
        return target

    def findPath(self, root, target):
        stack = []
        lastVisitor = None
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
                continue
            peek = stack[-1]
            if peek.right and lastVisitor != peek.right:
                root = root.right
                continue
            if peek == target:
                return stack
            lastVisitor = stack.pop()
            root = None
        return stack



if __name__ == '__main__':
    pass