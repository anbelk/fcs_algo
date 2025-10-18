from typing import Callable, TypeVar

R = TypeVar("R")

def tracer(func: Callable[..., R]) -> Callable[..., R]:
    def wrapper(*args, **kwargs) -> R:
        func(*args, **kwargs)
    return wrapper