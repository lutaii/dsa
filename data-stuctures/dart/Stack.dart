class Node<T> {
  T value;
  Node<T>? prev;

  Node(this.value);
}

class Stack<T> {
  int _length = 0;

  Node<T>? _head;

  Stack() {
    this._head = null;
  }

  int get length => _length;

  void push(T item) {
    _length++;
    Node<T> node = Node(item);
    if (_head == null) {
      _head = node;
    } else {
      node.prev = _head;
      _head = node;
    }
  }

  T? pop() {
    if (_head == null) {
      return null;
    } else {
      _length--;
      Node<T> head = _head!;
      _head = _head?.prev;
      head.prev = null;
      return head.value;
    }
  }

  T? peek() {
    return _head?.value;
  }
}

void main(List<String> args) {
  Stack<int> stack = Stack();
  print(stack.peek());
  print(stack.length);
  stack.pop();
  print(stack.peek());
  print(stack.length);
  stack.push(2);
  print(stack.peek());
  print(stack.length);
  stack.push(4);
  stack.push(15);
  print(stack.length);
  print(stack.pop());
  print(stack.pop());
  print(stack.pop());
  print(stack.peek());
  print(stack.pop());
  print(stack.length);
}
