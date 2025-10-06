import pytest
from hash_table_class import HashTable
from unittest.mock import patch

fixed_hashes = {
    'a': 3,
    'b': 0,
    'c': 1,
    'd': 3
}

def fake_hash(key):
    return fixed_hashes.get(key, 0)

def test_set():
    ht = HashTable()
    with patch('builtins.hash', side_effect=fake_hash):
        ht.set('a', 1)
        assert ht.count == 1
        assert ht.load_factor == 0.25
        assert ht.buckets == [None] * 3 + [['a', 1]]

def test_set_rehash():
    ht = HashTable()
    with patch('builtins.hash', side_effect=fake_hash):
        ht.set('a', 1)
        ht.set('b', 2)
        ht.set('c', 3)
        assert ht.capacity == 8
        assert ht.load_factor == 0.375

def test_get():
    ht = HashTable()
    with patch('builtins.hash', side_effect=fake_hash):
        with pytest.raises(KeyError):
            ht.get('a')
        ht.set('a', 1)
        assert ht.get('a') == 1

def test_delete():
    ht = HashTable()
    with patch('builtins.hash', side_effect=fake_hash):
        with pytest.raises(KeyError):
            ht.delete('a')
        ht.set('a', 1)
        ht.delete('a')
        assert ht.buckets == [None] * 3 + [["<deleted>", None]]
        assert ht.count == 0
        assert ht.load_factor == 0.25

def test_collitions():
    ht = HashTable()
    with patch('builtins.hash', side_effect=fake_hash):
        ht.set('a', 1)
        ht.set('d', 4)
        assert ht.buckets == [['d', 4]] + [None] * 2 + [['a', 1]]
