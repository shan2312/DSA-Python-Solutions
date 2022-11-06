NOT_FOUND = -1

class Node:
    def __init__(self, key, value):
        self.key, self.val = key, value
        self.prev = self.next = None



class LinkedList:
    def __init__(self, head = None, tail = None) -> None:
        self.head = head
        self.tail = tail

    def insert_at_front(self, node):
        node.next = self.head

        if self.head:
            self.head.prev = node

        node.prev = None
        self.head = node

        if self.tail is None:
            self.tail = self.head

    def delete(self, node):
        next_node, prev_node = node.next, node.prev

        if prev_node:
            prev_node.next = next_node

        if next_node:
            next_node.prev = prev_node

        if self.head == node:
            self.head = next_node

        if self.tail == node:
            self.tail = prev_node

    def move_to_front(self, node):
        is_at_front = node.prev is None
        if is_at_front:
            return

        self.delete(node)
        self.insert_at_front(node)



class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.cache = {}
        self.recently_used_keys = LinkedList()

    def get(self, key):
        if key not in self.cache:
            return NOT_FOUND

        node = self.cache[key]
        self.recently_used_keys.move_to_front(node)
        return node.val

    def delete_least_recently_used(self):
        least_recently_used_node = self.recently_used_keys.tail
        key = least_recently_used_node.key
        self.recently_used_keys.delete(least_recently_used_node)

        del self.cache[key]
        self.size -= 1


    def put(self, key, value):
        new_node = Node(key, value)

        if key in self.cache:
            old_node = self.cache[key]
            self.recently_used_keys.delete(old_node)

        else:
            if self.size == self.capacity:
                self.delete_least_recently_used()

            self.size += 1
        self.cache[key] = new_node
        self.recently_used_keys.insert_at_front(new_node)


