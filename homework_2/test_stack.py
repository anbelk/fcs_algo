import pytest

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
    
    def push(self, x):
        new_top = Node(x)
        new_top.next = self.top
        self.top = new_top
    
    def pop(self):
        if self.top:
            self.top = self.top.next
    
    def get_top(self):
        if self.top:
            return self.top.value
        return None
    
def test_stack_init():
    s = Stack()
    assert s.top is None

def test_stack_empty_push():
    s = Stack()
    s.push(5)
    assert s.top.value == 5 and s.top.next is None

def test_stack_filled_push():
    s = Stack()
    s.push(5)
    s.push(7)
    assert s.top.value == 7 and s.top.next.value == 5 and s.top.next.next is None

def test_stack_empty_pop():
    s = Stack()
    s.pop()
    assert s.top is None

def test_stack_filled_pop():
    s = Stack()
    s.push(5)
    s.pop()
    assert s.top is None
    s.push(5)
    s.push(3)
    s.pop()
    assert s.top.value == 5

def test_stack_empty_get_top():
    s = Stack()
    assert s.get_top() is None

def test_stack_filled_get_top():
    s = Stack()
    s.push(5)
    assert s.get_top() == 5

def test_stack_push_pop_top():
    s = Stack()
    s.push(2)
    s.push(5)
    s.pop()
    assert s.get_top() == 2
    s.push(9)
    assert s.get_top() == 9
    s.get_top()
    assert s.get_top() == 9
    s.pop()
    s.pop()
    s.pop()
    assert s.get_top() is None