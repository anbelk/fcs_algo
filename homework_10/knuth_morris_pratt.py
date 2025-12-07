# Сложность prefix_func по времени O(N), где N - длина строки.
# Объяснение:
#   Так как j увеличается максимум на 1 на каждом шаге, значит за весь цикл максимум N увеличений.
#   Из этого следует, что уменьшений тоже максимум N.
#   Поэтому внутренний цикл while суммарно делает не больше N шагов.
#   Цикл for тоже делает N шагов. Итоговая сложность O(N).
# Доппамять O(N) из-за массива pi.

def prefix_func(string):
    string_len = len(string)
    pi = [0] * string_len
    
    for i in range(1, string_len):
        j = pi[i - 1]

        while j > 0 and string[i] != string[j]:
            j = pi[j - 1]
        
        if string[i] == string[j]:
            j += 1
        pi[i] = j
    
    return pi

# Сложность КМП-алгоритма O(N + M), так как prefix_func считается за O(M), где M - длина подстроки, которую ищем,
# а цикл for за O(N), потому что внутренний цикл while по аналогичным prefix_func рассуждениям выполняется за O(N).
# Доппамять O(M + K), где K - число вхождений, за счет substring_pi O(M) и occurrences O(K).

def knuth_morris_pratt(string: str, substring_to_find: str) -> int:
    string_len = len(string)
    substring_len = len(substring_to_find)

    occurrences = []
    substring_pi = prefix_func(substring_to_find)

    j = 0
    for i in range(string_len):
        while j > 0 and string[i] != substring_to_find[j]:
            j = substring_pi[j - 1]
        
        if string[i] == substring_to_find[j]:
            j += 1
        
        if j == substring_len:
            occurrences.append(i - substring_len + 1)
            j = substring_pi[j - 1]

    return occurrences