import unittest
from doubly_node import DoublyNode

class DoublyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def __isempty__(self):
        if self.head is None:
            return True
        return False

    def append(self, x):
        new_node = DoublyNode(x)
        if self.__isempty__():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, x):
        new_node = DoublyNode(x)
        if self.__isempty__():
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
    
    def pop(self):
        if not self.__isempty__():
            if self.tail.prev is None:
                self.head = None
                self.tail = None
            else:
                self.tail = self.tail.prev
                self.tail.next = None

    def pop_front(self):
        if not self.__isempty__():
            if self.head.next is None:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None

    def get_head(self):
        if not self.__isempty__():
            return self.head.value
        return None
        
    def get_tail(self):
        if not self.__isempty__():
            return self.tail.value
        return None

class TestDoublyLinkedList(unittest.TestCase):
    def test_one_append(self):
        dll = DoublyLinkedList()
        dll.append(5)
        self.assertIs(dll.head, dll.tail)
        self.assertEqual(dll.head.value, 5)
        self.assertIsNone(dll.head.next)
        self.assertIsNone(dll.head.prev)

    def test_double_append(self):
        dll = DoublyLinkedList()
        dll.append(5)
        dll.append(9)
        self.assertEqual(dll.head.value, 5)
        self.assertIsNone(dll.head.prev)
        self.assertEqual(dll.head.next, dll.tail)
        self.assertEqual(dll.tail.value, 9)
        self.assertEqual(dll.tail.prev, dll.head)
        self.assertIsNone(dll.tail.next)
    
    def test_one_prepend(self):
        dll = DoublyLinkedList()
        dll.prepend(5)
        self.assertIs(dll.head, dll.tail)
        self.assertEqual(dll.head.value, 5)
        self.assertIsNone(dll.head.next)
        self.assertIsNone(dll.head.prev)

    def test_double_prepend(self):
        dll = DoublyLinkedList()
        dll.prepend(5)
        dll.prepend(9)
        self.assertEqual(dll.head.value, 9)
        self.assertIsNone(dll.head.prev)
        self.assertEqual(dll.head.next, dll.tail)
        self.assertEqual(dll.tail.value, 5)
        self.assertEqual(dll.tail.prev, dll.head)
        self.assertIsNone(dll.tail.next)

    def test_pop_empty(self):
        dll = DoublyLinkedList()
        dll.pop()
        self.assertIsNone(dll.head)
        self.assertIsNone(dll.tail)

    def test_pop_filled(self):
        dll = DoublyLinkedList()
        dll.append(7)
        dll.pop()
        self.assertIsNone(dll.head)
        self.assertIsNone(dll.tail)
        dll.append(3)
        dll.prepend(4)
        dll.pop()
        self.assertIs(dll.head, dll.tail)
        self.assertEqual(dll.head.value, 4)
        self.assertIsNone(dll.head.next)
        self.assertIsNone(dll.head.prev)
    
    def test_pop_front_empty(self):
        dll = DoublyLinkedList()
        dll.pop_front()
        self.assertIsNone(dll.head)
        self.assertIsNone(dll.tail)

    def test_pop_front_filled(self):
        dll = DoublyLinkedList()
        dll.append(7)
        dll.pop_front()
        self.assertIsNone(dll.head)
        self.assertIsNone(dll.tail)
        dll.prepend(3)
        dll.append(4)
        dll.pop_front()
        self.assertIs(dll.head, dll.tail)
        self.assertEqual(dll.head.value, 4)
        self.assertIsNone(dll.head.next)
        self.assertIsNone(dll.head.prev)

    def test_get_head_empty(self):
        dll = DoublyLinkedList()
        self.assertIsNone(dll.get_head())

    def test_get_head_filled(self):
        dll = DoublyLinkedList()
        dll.append(7)
        self.assertEqual(dll.get_head(), 7)
        dll.prepend(3)
        self.assertEqual(dll.get_head(), 3)

    def test_get_tail_empty(self):
        dll = DoublyLinkedList()
        self.assertIsNone(dll.get_tail())

    def test_get_tail_filled(self):
        dll = DoublyLinkedList()
        dll.append(7)
        self.assertEqual(dll.get_tail(), 7)
        dll.append(3)
        self.assertEqual(dll.get_tail(), 3)

if __name__ == "__main__":
    unittest.main()