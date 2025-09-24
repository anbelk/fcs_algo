import pytest

def num_primes_less_N(N: int) -> int:
    is_prime_arr = [1] * N
    for num in range(2, N):
        if is_prime_arr[num]:
            multiple_factor = 2
            next_multiple_num = num * multiple_factor
            while next_multiple_num < N:
                is_prime_arr[next_multiple_num] = 0
                multiple_factor += 1
                next_multiple_num = num * multiple_factor
    return sum(is_prime_arr[2:])

def test_one():
    assert num_primes_less_N(1) == 0

def test_two():
    assert num_primes_less_N(2) == 0

def test_three():
    assert num_primes_less_N(3) == 1

def test_big_num():
    assert num_primes_less_N(13) == 5