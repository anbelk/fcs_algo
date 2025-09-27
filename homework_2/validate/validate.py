import unittest
from stack_vs_queue.stack import Stack

def validate(pushed: list, popped: list) -> bool:
    num_operations = len(pushed)
    s = Stack()
    i = j = 0
    while True:
        if j == num_operations:
            break
        elif i == num_operations:
            if popped[j] != s.get_top():
                return False
            s.pop()
            j += 1
        elif popped[j] == s.get_top():
            s.pop()
            j += 1
        elif popped[j] == pushed[i]:
            i += 1
            j += 1
        else:
            s.push(pushed[i])
            i += 1
    return True

class TestValidate(unittest.TestCase):
    def test_empty(self):
        self.assertTrue(validate([], []))
    
    def test_one_elem(self):
        self.assertTrue(validate([1], [1]))

    def test_first_example(self):
        self.assertTrue(validate([1, 2, 3, 4, 5], [1, 3, 5, 4, 2]))

    def test_second_example(self):
        self.assertFalse(validate([1, 2, 3], [3, 1, 2]))
    
    def test_third_example(self):
        self.assertFalse(validate([5, 2, 4, 3], [2, 3, 5, 4]))

    def test_fourth_example(self):
        self.assertTrue(validate([4, 7, 5, 1, 2], [5, 7, 1, 2, 4]))
        # push(4) push(7) push(5) pop(5) pop(7) push(1) pop(1) push(2) pop(2) pop(4)

if __name__ == "__main__":
    unittest.main()