class Node:
    def __init__(self, val: int, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def prepend(self, item: int):
        node = Node(val=item)
        
        self.length += 1
        if not self.head:
            self.head = self.tail = node  
            return
        
        node.next = self.head
        self.head.prev = node
        self.head = node
    
    def insertAt(self, item: int, idx: int):
        if idx > self.length:  
            print('Idx > length')
            return
        
        if (idx == self.length):
            self.append(item=item)
            return
        elif (idx == 0):
            self.prepend(item=item)
            return
        
        self.length += 1
        curr = self.__getAt(idx=idx)
        
        node = Node(val=item)
        node.next = curr
        node.prev = curr.prev
        curr.prev = node
        if node.prev:
            node.prev.next = node
    
    def append(self, item: int):
        node = Node(val=item)

        self.length += 1
        if not self.tail:
            self.head = self.tail = node  
            return
        
        node.prev = self.tail
        self.tail.next = node
        self.tail = node
    
    def remove(self, item: int):
        curr = self.head
        for _ in range(0, self.length):
            if curr.next:
                curr = curr.next
            if curr.val == item:
                break
        if not curr:
            return

        return self.__removeNode(curr)
        
    def get(self, idx: int):
        node =  self.__getAt(idx=idx)
        if not node:
            return None
        return node.val
    
    def removeAt(self, idx: int):
        node = self.__getAt(idx=idx)
        if not node:
            return None
        return self.__removeNode(node)

    def __removeNode(self, node: Node):

        self.length -= 1
        
        if self.length == 0:
            out = self.head.val
            self.head = self.tail = None
            return out
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev

        if node == self.head:
            self.head = node.next
        if node == self.tail:
            self.tail = node.prev

        node.prev = node.next = None
        return node.val
    
    def __getAt(self, idx: int):
        curr = self.head
        for _ in range(0, idx):
            if not curr.next:
                return None
            curr = curr.next 
        return curr
    

dll = DoublyLinkedList()
print(dll.length)
dll.append(5)
print(dll.length)
print(dll.head.val)
print(dll.tail.val)
dll.prepend(10)
print(dll.head.val)
print(dll.tail.val)
dll.prepend(11)
print(dll.head.val)
print(dll.tail.val)
dll.append(2)
print(dll.head.val)
print(dll.tail.val)
print(dll.insertAt(13, 4))
print(dll.get(1))
dll.removeAt(4)
print(dll.length)
print(dll.get(0))