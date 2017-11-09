# Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class ListCycle(object):
    def solution1(self, root):
        if not root:
            return None
        cur = root.next
        isCycle = False
        while cur:
            if cur == root:
                isCycle = True
                break
            cur = cur.next
        return root if isCycle else None


if __name__ == '__main__':
    pass