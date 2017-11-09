# Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class ListCycle(object):
    def solution1(self, root):
        if not root or not root.next:
            return None
        slow, fast = root, root
        while slow and fast:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow1 = root
                while slow1 != slow:
                    slow1 = slow1.next
                    slow = slow.next
                return slow1
        return None


if __name__ == '__main__':
    pass