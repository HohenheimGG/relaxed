# Merge two sorted linked lists and return it as a new list.
# The new list should be made by splicing together the nodes of the first two lists.


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class MergeTwoSortedList:
    def solution1(self, list1, list2):
        if not list1 and list2:
            return None
        if not list1:
            return list2
        if not list2:
            return list1

        node = start = ListNode(0)
        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next

        node.next = list1 or list2
        return start.next

    def solution2(self, list1, list2):
        if not list1 and list2:
            return None
        if not list1:
            return list2
        if not list2:
            return list1
        return self.recursive(list1, list2)

    def recursive(self, list1, list2):
        if not list1:
            return list2
        if not list2:
            return list2

        if list1.val < list2.val:
            list1.next = self.recursive(list1.next, list2)
            return list1
        else:
            list2.next = self.recursive(list1, list2.next)
            return list2

if __name__ == "__main__":
    a = ListNode(0, ListNode(3, ListNode(5, ListNode(8))))
    b = ListNode(2, ListNode(3, ListNode(4, ListNode(6))))
    result = MergeTwoSortedList().solution1(a, b)
    while result is not None:
        print result.val
        result = result.next

