import time
import random
import matplotlib.pyplot as plt
from makeheap import makeheap, makeheap_n_log_n


def benchmark(func, arr):
    start = time.perf_counter()
    func(arr.copy())
    return time.perf_counter() - start


def main():
    sizes = [5_000, 10_000, 20_000, 50_000, 100_000, 200_000, 400_000, 600_000]

    times_nlogn = []
    times_n = []

    for n in sizes:
        arr = [random.randint(0, 10**6) for _ in range(n)]

        t1 = benchmark(makeheap_n_log_n, arr)
        t2 = benchmark(makeheap, arr)

        times_nlogn.append(t1)
        times_n.append(t2)

        print(f"n={n} processed: T(makeheap_n_log_n)={t1:.5f} s, T(makeheap)={t2:.5f} s")

    plt.figure(figsize=(10, 6))
    plt.plot(sizes, times_nlogn, marker="o", label="makeheap_n_log_n (O(N log N))")
    plt.plot(sizes, times_n, marker="o", label="makeheap (O(N))")

    plt.title("Сравнение времени работы алгоритмов построения кучи")
    plt.xlabel("Размер массива (N)")
    plt.ylabel("Время (секунды)")
    plt.grid(True)
    plt.legend()

    plt.savefig("pics/compare_makeheap_algorithms.png", dpi=200)
    plt.show()


if __name__ == "__main__":
    main()
