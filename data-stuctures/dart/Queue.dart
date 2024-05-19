class Node<T> {
  T value;
  Node<T>? next;

  Node(this.value);
}

class Queue<T> {
  int _length = 0;

  Node<T>? _head;

  Node<T>? _tail;

  Queue() {
    this._head = null;
    this._tail = null;
  }

  int get length => _length;

  void enqueue(T item) {
    _length++;
    Node<T> node = Node(item);
    if (_tail != null) {
      _tail?.next = node;
      _tail = node;
    } else {
      _tail = node;
      _head = _tail;
    }
  }

  T? deque() {
    if (_head == null) {
      return null;
    } else {
      this._length--;
      Node<T> head = _head!;
      _head = _head?.next;
      head.next = null;
      if (_length == 0) {
        _tail = null;
      }
      return head.value;
    }
  }

  T? peek() {
    return _head?.value;
  }
}

void main(List<String> args) {
  Queue<int> queue = Queue();

  queue.enqueue(5);

  print(queue.length);

  queue.enqueue(7);

  queue.enqueue(12);

  print(queue.length);

  print(queue.deque());

  print(queue.peek());

  print(queue.deque());

  print(queue.peek());

  print(queue.deque());

  print(queue.deque());

  print(queue.peek());
}
