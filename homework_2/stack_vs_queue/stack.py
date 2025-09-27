import unittest
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.dll = DoublyLinkedList()
    
    def __isempty__(self):
        return self.dll.__isempty__()
    
    def push(self, x):
        self.dll.append(x)
    
    def pop(self):
        self.dll.pop()
    
    def get_top(self):
        return self.dll.get_tail()
    
class TestStack(unittest.TestCase):
    def test_stack(self):
        s = Stack()
        s.push(1)
        s.push(3)
        s.pop()
        s.push(2)
        self.assertEqual(s.get_top(), 2)
        s.pop()
        self.assertEqual(s.get_top(), 1)
        s.pop()
        self.assertIsNone(s.get_top())

if __name__ == "__main__":
    unittest.main()