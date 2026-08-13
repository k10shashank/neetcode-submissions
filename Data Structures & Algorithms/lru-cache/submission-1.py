class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def add_to_front(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def remove_from_mid(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = None
        node.prev = None

    def remove_from_back(self):
        sec_last = self.tail.prev
        sec_last.prev.next = self.tail
        self.tail.prev = sec_last.prev
        sec_last.prev = None
        sec_last.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = dict()
        self.size = 0
        self.capacity = capacity
        self.dll = DoubleLinkedList()

    def get(self, key: int) -> int:
        if self.cache.get(key) is None:
            return -1
        else:
            node = self.cache[key]
            self.dll.remove_from_mid(node)
            self.dll.add_to_front(node)
            return node.value
        

    def put(self, key: int, value: int) -> None:
        if self.cache.get(key) is None:
            if self.size == self.capacity:
                self.cache.pop(self.dll.tail.prev.key)
                self.dll.remove_from_back()
                self.size -= 1
            self.cache[key] = Node(key, value)
            self.dll.add_to_front(self.cache[key])
            self.size += 1
        else:
            self.cache[key].value = value
            self.dll.remove_from_mid(self.cache[key])
            self.dll.add_to_front(self.cache[key])