def tracer(func):
    def wrapper(*args, **kwargs):
        wrapper.depth += 1
        indent = "  " * (wrapper.depth - 1)
        print(f"{indent}--> {func.__name__}{args}")
        result = func(*args, **kwargs)
        print(f"{indent}<-- {func.__name__}{args} = {result}")
        wrapper.depth -= 1
        return result
    wrapper.depth = 0
    return wrapper