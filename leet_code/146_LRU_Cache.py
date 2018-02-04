 # Design and implement a data structure for Least Recently Used (LRU) cache.
 # It should support the following operations: get and put.
#
# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present.
 # When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
#
# Follow up:
# Could you do both operations in O(1) time complexity?
#

class LRUCache(object):

    class Node(object):
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.next, self.prev = None, None

    def __init__(self, capacity):
        self.capacity, self.size = capacity, 0
        self.dict = {}
        self.head, self.tail = self.Node(-1, -1), self.Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def set(self, key, value):
        if key in self.dict:
            node = self.dict[key]
            self._remove(node)
            node.value = value
            self._insert(node)
        else:
            if self.size == self.capacity:
                discard = self.tail.prev
                self._remove(discard)
                self.size -= 1
                del self.dict[discard.key]
                discard.prev, discard.next = None, None
            node = self.Node(key, value)
            self._insert(node)
            self.dict[key] = node
            self.size += 1

    def get(self, key):
        if key not in self.dict:
            return -1
        node = self.dict[key]
        self._remove(node)
        self._insert(node)
        return node.value

    def _remove(self, node):
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node

    def _insert(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

if __name__ == '__name__':
    pass
