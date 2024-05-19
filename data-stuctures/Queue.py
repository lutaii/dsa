class Node:
    def __init__(self, val: int, next=None):
        self.val = val
        self.next = next

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def enqueue(self, val: int):
        node = Node(val=val)
        self.length += 1
        if not self.tail:
            self.tail = node
            self.head = self.tail
        else:
            self.tail.next = node
            self.tail = node
    
    def dequeue(self):
        if not self.head:
            return None
        else:
            self.length -= 1
            tempHead = self.head
            self.head = self.head.next
            tempHead.next = None
            if self.length == 0:
                self.tail = None
            return tempHead.val
    
    def peek(self):
        if self.head:
            return self.head.val
        return None


que = Queue()

print(que.dequeue())
print(que.length)
que.enqueue(5)
print(que.dequeue())
print(que.length)
que.enqueue(5)
que.enqueue(7)
que.enqueue(2)
print(que.length)
print(que.peek())
print(que.dequeue())
print(que.dequeue())
print(que.length)
print(que.peek())
print(que.dequeue())
print(que.peek())