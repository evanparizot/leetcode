class LRUCache():
    def __init__(self, capacity: int):
        self.cache = {}
        self.size = 0
        self.capacity = capacity
        self.head, self.tail = Node(), Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        node = self.cache.get(key, None)
        if not node:
            return -1

        self._move_to_head(node)
        return node.val


    def put(self, key: int, value: int) -> None:
            
        # Replace node at head with new node
        # Check if we need to evict nodes (cache is full)

        # Store pointer to node in dictionary
        node = self.cache.get(key)
        if not node:
            new = Node()
            new.key = key
            new.val = value

            self.cache[key] = new
            self._add_node(new)

            self.size += 1

            if self.size > self.capacity:
                tail = self._pop_tail()
                del self.cache[tail.key]
                self.size -= 1
        else:
            node.val = value
            self._move_to_head(node)


    def _add_node(self, node):
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        prev = node.prev
        new = node.next

        prev.next = new
        new.prev = prev

    def _move_to_head(self, node):
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self):
        res = self.tail.prev
        self._remove_node(res)
        return res

class Node():
    def __init__(self):
        self.key = 0
        self.val = 0
        self.prev = None
        self.next = None

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
from collections import OrderedDict
class LRUCache2(OrderedDict):
    def __init__(self, capacity):
        self.capacity = capacity
    
    def get(self, key):
        if key not in self:
            return -1
        self.move_to_end(key)
        return self[key]

    def put(self, key, value):
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last = False)

class LRUCache3():
    def __init__(self, capacity):
        self.capacity = capacity
        self.dictionary = OrderedDict()

    def get(self, key):
        if key not in self.dictionary:
            return -1
        self.dictionary.move_to_end(key)
        return self.dictionary[key]

    def put(self, key, value):
        if key in self.dictionary:
            self.dictionary.move_to_end(key)
        self.dictionary[key] = value
        if len(self.dictionary) > self.capacity:
            self.dictionary.popitem(last = False)