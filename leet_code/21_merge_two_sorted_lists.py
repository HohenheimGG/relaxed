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

        node = None
        start = None
        while list1 and list2 :
            if node is None:
                if list1.val < list2.val:
                    node = list1
                    list1 = list1.next
                elif list2.val < list1.val:
                    node = list2
                    list2 = list2.next
                else:
                    node = list1
                    list1 = list1.next
                    node.next = list2
                    list2 = list2.next
                    node = node.next
                start = node
                continue

            if list1 is None or list2 is None:
                node.next = list1 if list2 is None else list2
                break

            if list1.val > list2.val:
                node.next = list2
                list2 = list2.next
            elif list2.val > list1.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list1
                list1 = list1.next
                node.next.next = list2
                list2 = list2.next
                node = node.next
            node = node.next
        return start

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

