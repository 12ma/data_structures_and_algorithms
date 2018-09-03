from .node import Node


class Queue(object):
    def __init__(self, iterable=[]):
        """An instance method of the queue object. """
        self.front: Node = None
        self.rear: Node = None
        self._val = None
        self._length: int = 0
        for i in iterable:
            self.enqueue(i)

    def __str__(self):
        """A string representation of the queue object. """
        return f'Front: {self.front} | Length: {self._length}'

    def __repr__(self):
        """An 'official' string reputation of the queue object. """
        return f'<Queue | Front: {self.front} | Length: {self._length}'

    def __len__(self):
        """The length of the queue. """
        return self._length

    def enqueue(self, val):
        """Accepts a value as an argument and adds that value to the rear of the queue. """
        try:
            temp = self.rear
            self.rear = Node(val, self.rear)
            temp._next = self.rear
        except AssertionError:
            self.rear = Node(val, self.rear)
        self._length += 1

    def dequeue(self):
        """Removes the Node at the front of the queue, otherwise front is none. """
        try:
            temp = self.front
            self.front = temp._next
            temp._next = None
            self._length -= 1
            return temp
        except AttributeError:
            self.front = None
            self._length = 0
            return "No node in the queue"

    def peek(self):
        """This method looks at the node at the front. """
        try:
            return self.front
        except AttributeError:
            return "There is no node in the stack"



