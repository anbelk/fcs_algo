import pytest
from tracer_decorator import tracer

@tracer()
def fib(n: int) -> int:
    if n == 1:
        return 1
    return n * fib(n - 1)

def test_tracer():
    pass