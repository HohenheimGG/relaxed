
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class AddTwoNumbers:
    def solution1(self, l1, l2):
        """
        :type l1: ListNode 
        :type l2: ListNode
        :return: 
        """
        if(not l1 or not l2):
            return None
        l3 = ListNode(0)
        current, digit = l3, 0

        while(l1 or l2):
            val = digit
            if(l1):
                val += l1.val
                l1 = l1.next
            if(l2):
                val += l2.val
                l2 = l2.next
            if(val >= 10):
                digit = 1
                current.next = ListNode(val % 10)
            else:
                digit = 0
                current.next = ListNode(val)
            current = current.next


        if(digit == 1):
            current.next = ListNode(1)

        return l3.next;

if __name__ == '__main__':
    a, a.next, a.next.next = ListNode(2), ListNode(4), ListNode(3)
    b, b.next, b.next.next = ListNode(5), ListNode(6), ListNode(4)
    result = AddTwoNumbers().solution1(a, b)
    print "{0} -> {1} -> {2}".format(result.val, result.next.val, result.next.next.val)