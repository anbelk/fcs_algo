# В качестве rolling hash для подстроки длины m используем полиномиальный хэш
# ord(s[start_idx]) * B ** (m - 1) + ord(s[start_idx + 1]) * B ** (m - 2) + ... + ord(s[start_idx + m - 1]),
# так как он удобен для пересчёта при сдвиге начала подстроки start_idx.
# Достаточно лишь вычесть вклад от s[start_idx - 1], так как он исключается из подстроки,
# домножить хэш на B
# и добавить вклад от нового символа s[start_idx + m].

# Сложность по времени O(string_len + substring_to_find) при отсутствии коллизий.
# Доппамять O(K), где K - число вхождений.

def rabin_karp(string: str, substring_to_find: str) -> int:
    B = 256
    M = int(1e9) + 7

    string_len = len(string)
    substring_len = len(substring_to_find)

    if substring_len == 0:
        return [0]
    elif substring_len > string_len:
        return []
    
    out_coeff = pow(B, substring_len - 1, M)
    

    def hashify(string):
        string_hash = 0

        for i in range(substring_len):
            string_hash += ord(string[i]) * pow(B, substring_len - i - 1, M)

        string_hash %= M

        return string_hash
    
    
    def rehash(old_hash, out_idx):
        new_hash = (old_hash - out_coeff * ord(string[out_idx])) * B + ord(string[out_idx + substring_len])
        new_hash %= M

        return new_hash


    substring_to_find_hash = hashify(substring_to_find)
    substring_hash = hashify(string[:substring_len])

    occurrences = []

    if substring_hash == substring_to_find_hash and string[:substring_len] == substring_to_find:
        occurrences.append(0)

    for start_idx in range(1, string_len - substring_len + 1):
        substring_hash = rehash(substring_hash, start_idx - 1)

        if substring_hash == substring_to_find_hash:
            if string[start_idx : start_idx + substring_len] == substring_to_find:
                occurrences.append(start_idx)

    return occurrences