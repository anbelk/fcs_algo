import unittest
from node import Node
from linked_list import LinkedList

# in-place
def merge_lists_dummy(list1: LinkedList, list2: LinkedList) -> LinkedList:
    curr1 = list1.head
    curr2 = list2.head
    curr3 = dummy = Node()
    while curr1 is not None and curr2 is not None:
        if curr1.value <= curr2.value:
            curr3.next = curr1
            curr1 = curr1.next
        else:
            curr3.next = curr2
            curr2 = curr2.next
        curr3 = curr3.next
    if curr1 is None and curr2 is not None:
        curr3.next = curr2
    if curr2 is None and curr1 is not None:
        curr3.next = curr1
    list3 = LinkedList()
    list3.head = dummy.next
    return list3

class TestMergeListsDummy(unittest.TestCase):
    def test_empty_lists(self):
        list1 = LinkedList([])
        list2 = LinkedList([])
        list3 = LinkedList([])
        self.assertEqual(merge_lists_dummy(list1, list2).to_python_list(), list3.to_python_list())

    def test_first_list_only(self):
        list1 = LinkedList([1, 2, 3])
        list2 = LinkedList([])
        list3 = LinkedList([1, 2, 3])
        self.assertEqual(merge_lists_dummy(list1, list2).to_python_list(), list3.to_python_list())

    def test_second_list_only(self):
        list1 = LinkedList([])
        list2 = LinkedList([1, 2])
        list3 = LinkedList([1, 2])
        self.assertEqual(merge_lists_dummy(list1, list2).to_python_list(), list3.to_python_list())
    
    def test_first_example(self):
        list1 = LinkedList([1, 2, 4])
        list2 = LinkedList([1, 3, 4])
        list3 = LinkedList([1, 1, 2, 3, 4, 4])
        self.assertEqual(merge_lists_dummy(list1, list2).to_python_list(), list3.to_python_list())
    
    def test_second_example(self):
        list1 = LinkedList([2, 3, 5, 6])
        list2 = LinkedList([1, 4])
        list3 = LinkedList([1, 2, 3, 4, 5, 6])
        self.assertEqual(merge_lists_dummy(list1, list2).to_python_list(), list3.to_python_list())

if __name__ == "__main__":
    unittest.main()