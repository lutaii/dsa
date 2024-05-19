from typing import Optional

class BinaryNode:
    def __init__(self, val: int) -> None:
        self.val = val
        self.left = None
        self.right = None

#              5
#        3               7
#    23     25      0         66
        

def walk(curr: Optional[BinaryNode], path: list):
    if not curr:
        return
    
    walk(curr.left, path)
    walk(curr.right, path)
    path.append(curr.val)

    return path


def pre_order(head: BinaryNode):

    return walk(head, [])

head = BinaryNode(val=5)
head.left = BinaryNode(val=3)
head.right = BinaryNode(val=7)
head.left.left = BinaryNode(val=23)
head.left.right = BinaryNode(val=25)
head.right.left = BinaryNode(val=0)
head.right.right = BinaryNode(val=66)

print(pre_order(head))