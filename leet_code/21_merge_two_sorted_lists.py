# Merge two sorted linked lists and return it as a new list.
# The new list should be made by splicing together the nodes of the first two lists.

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MergeTwoSortedList:
    def solution1(self, list1, list2):
        if not list1 and list2:
            return None
        if not list1:
            return list2
        if not list2:
            return list1

        node = None
        while not list1 and not list2:
            if list1 is None:
                node.next = list1
                break
            elif list2 is None:
                node.next = list2
                break






if __name__ == "__main__":
    pass
