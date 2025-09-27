import unittest
from doubly_linked_list import DoublyLinkedList

class Queue():
    def __init__(self):
        self.dll = DoublyLinkedList()

    def enqueue(self, x):
        self.dll.append(x)

    def dequeue(self):
        self.dll.pop_front()

    def peek(self):
        return self.dll.get_head()
    
class TestQueue(unittest.TestCase):
    def test_queue_init(self):
        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        self.assertEqual(q.peek(), 1)
        q.dequeue()
        self.assertEqual(q.peek(), 2)
        q.dequeue()
        self.assertIsNone(q.peek())

if __name__ == "__main__":
    unittest.main()