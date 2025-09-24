import pytest

def is_palindrome(x: int) -> bool:
    x_copy = x
    x_inv = 0
    while x:
        x_inv = x_inv * 10 + x % 10
        x //= 10
    return x_inv == x_copy

def test_zero():
    assert is_palindrome(0) is True

def test_not_palindrome():
    assert is_palindrome(123) is False

def test_even_palindrome():
    assert is_palindrome(13455431) is True

def test_odd_palindrome():
    assert is_palindrome(124525421) is True