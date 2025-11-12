import time
import random
from quicksort import quicksort_rec
from mergesort import mergesort_rec

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__}: {end - start:.6f} с")
        return result
    return wrapper

N = 900
random_array = random.sample(range(N), N)
sorted_array = list(range(N))

print("Случайный массив")
timer(mergesort_rec)(random_array.copy())
timer(quicksort_rec)(random_array.copy())

print("\nОтсортированный массив (худший случай для quicksort с pivot = первый элемент)")
timer(mergesort_rec)(sorted_array.copy())
timer(quicksort_rec)(sorted_array.copy())
