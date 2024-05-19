class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def get(self, index: int) -> int:
        if index >= self.length:
            return -1
        curr = self.head
        for _ in range(0, index):
            if not curr:
                return -1
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        node = Node(val=val)
        
        if not self.tail:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head = node

        self.length += 1

    def addAtTail(self, val: int) -> None:
        node = Node(val=val)
        
        if not self.head:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length:
            return
        if index == 0:
            self.addAtHead(val)
            return
        if index == self.length:
            self.addAtTail(val)
            return
        curr = self.head
        node = Node(val=val)
        for _ in range(0, index-1):
            if not curr:
                return
            curr = curr.next
        node.next = curr.next
        curr.next = node

        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.length:
            return
        if index == 0:
            self.length -= 1
            self.head = self.head.next
            return
        curr = self.head
        for _ in range(0, index-1):
            if not curr:
                return
            curr = curr.next
        if curr.next:
            curr.next = curr.next.next
        if index == self.length - 1:
            self.tail = curr
        
        self.length -= 1
        if self.length == 0:
            self.head = self.tail = None
            return
