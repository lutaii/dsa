class Node:
    def __init__(self, val: int, prev=None):
        self.val = val
        self.prev = prev

class MinStack:

    def __init__(self):
        self.head = None
        self.minHead = None

    def push(self, val: int) -> None:
        node = Node(val=val)
        if not self.head:
            self.head = node
            self.minHead = node
        else:
            node.prev = self.head
            self.head = node
            minNode = Node(val=min(self.minHead.val, node.val))
            minNode.prev = self.minHead
            self.minHead = minNode  

    def pop(self) -> None:
        if self.head:
            self.head = self.head.prev
            self.minHead = self.minHead.prev        
        

    def top(self) -> int:
        return self.head.val
        

    def getMin(self) -> int:
        return self.minHead.val
        


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(5)
obj.push(7)
obj.push(6)
obj.push(4)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()
print(param_3, param_4)