# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.


class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class MergeKLists(object):
    def solution1(self, lists):
        if not lists:
            return None
        length = len(lists)
        if length == 1:
            return lists[0]

        is_odd = length % 2 == 1
        if is_odd:
            length -= 1
        while length != 1:
            index = 0
            count = 0
            while index < length:
                lists[count] = self.mergeTwoList(lists[index], lists[index + 1])
                index += 2
                count += 1
            length /= 2
        if is_odd:
            lists[0] = self.mergeTwoList(lists[0], lists[len(lists) - 1])
        return lists[0]

    def mergeTwoList(self, list1, list2):
        if not list1:
            return list2
        if not list2:
            return list1
        start = cur = ListNode(0)
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        cur.next = list1 or list2
        return start.next


if __name__ == '__main__':
    a = ListNode(0, ListNode(3, ListNode(5, ListNode(8))))
    b = ListNode(2, ListNode(3, ListNode(6, ListNode(9))))
    c = ListNode(1, ListNode(7, ListNode(10, ListNode(14))))
    d = ListNode(4, ListNode(5, ListNode(13, ListNode(18))))
    e = ListNode(19, ListNode(20, ListNode(21, ListNode(22))))
    result = MergeKLists().solution1([a, b, c, d, e])
    while result:
        print result.val
        result = result.next

