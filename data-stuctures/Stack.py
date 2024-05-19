class Node:
    def __init__(self, val: int, prev=None):
        self.val = val
        self.prev = prev

class Stack:
    def __init__(self):
        self.head = None
        self.length = 0

    def push(self, val: int):
        node = Node(val= val)
        self.length += 1
        if not self.head:
            self.head = node
        else:
            node.prev = self.head
            self.head = node

    def pop(self):
        if self.head:
            self.length -= 1
            self.head = self.head.prev  

    def top(self):
        if self.head:
            return self.head.val
        return None
        


# Your MinStack object will be instantiated and called as such:
obj = Stack()
obj.push(5)
obj.push(7)
obj.push(6)
obj.push(4)
obj.pop()
obj.pop()
param_3 = obj.top()
print(obj.length)