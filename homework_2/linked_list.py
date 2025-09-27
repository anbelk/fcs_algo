import unittest
from node import Node

class LinkedList():
    def __init__(self, python_list=None):
        if python_list is None:
            self.head = None
        else:
            dummy = Node()
            elem = dummy
            for idx in range(len(python_list)):
                new_node = Node(value=python_list[idx])
                elem.next = new_node
                elem = elem.next
            self.head = dummy.next

    def __isempty__(self):
        if self.head is None:
            return True
        return False
    
    def to_python_list(self):
        python_list = []
        elem = self.head
        while elem is not None:
            python_list.append(elem.value)
            elem = elem.next
        return python_list
    
class TestLinkedList(unittest.TestCase):
    def test_init_empty(self):
        ll = LinkedList()
        self.assertIsNone(ll.head)

    def test_init_filled(self):
        ll = LinkedList([1, 2])
        self.assertEqual(ll.head.value, 1)
        self.assertEqual(ll.head.next.value, 2)
        self.assertIsNone(ll.head.next.next)

if __name__ == "__main__":
    unittest.main()