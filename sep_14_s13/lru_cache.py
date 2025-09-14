class Node:
    def __init__(self, key, value, nex=None, prev=None):
        self.key = key
        self.value = value
        self.next = nex
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.head = Node(0,0) # dummy pointers
        self.tail = Node(0,0) # dummy pointers
        self.head.next, self.tail.prev = self.tail, self.head

    def __insert_at_head(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        
    def __remove(self, node):
        # can be both tail or a node
        node.prev.next = node.next
        node.next.prev = node.prev
        
    def get(self, key: int) -> int:
        if self.cache.get(key, None) is None:
            return -1 
        node = self.cache.get(key)
        self.__remove(node)
        self.__insert_at_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        # if already there then update the value
        if self.cache.get(key, None):
            node = self.cache[key]
            node.value = value
            self.__remove(node)
            self.__insert_at_head(node)
        else:
            # check if capacity is there
            new_node = Node(key, value)
            if len(self.cache) >= self.capacity:
                to_remove = self.tail.prev
                self.__remove(to_remove)
                self.cache.pop(to_remove.key)
            self.__insert_at_head(new_node)
            self.cache[key] = new_node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)