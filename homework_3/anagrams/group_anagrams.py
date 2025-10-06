import pytest

def group_anagrams(strs: list) -> list:
    strs_map = {}
    for word in strs:
        chars = ''.join(sorted(word))
        if chars in strs_map:
            strs_map[chars].append(word)
        else:
            strs_map[chars] = [word]
    return list(strs_map.values())

@pytest.mark.parametrize(
    "input,output",
    [
        (
            [],
            [],
        ),
    
        (
            [""],
            [[""]],
        ),
        
        (
            ["a"],
            [["a"]],
        ),

        (
            ["abc", "abc", "cab", "bca"],
            [["abc", "abc", "cab", "bca"]],
        ),

        (
            ["dog", "cat", "fish"],
            [["dog"], ["cat"], ["fish"]],
        ),

        (
            ["a", "ab", "ba", "abc", "cab"],
            [["a"], ["ab", "ba"], ["abc", "cab"]],
        ),

        (
            ["aabb", "baba", "bbaa", "abab", "aaab"],
            [["aabb", "baba", "bbaa", "abab"], ["aaab"]],
        ),

        (
            ["eat", "tea", "tan", "ate", "nat", "bat"],
            [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
        ),
    ],
)
def test_group_anagrams(input, output):
    result = group_anagrams(input)
    result_sorted = sorted([sorted(group) for group in result])
    output_sorted = sorted([sorted(group) for group in output])
    assert result_sorted == output_sorted
