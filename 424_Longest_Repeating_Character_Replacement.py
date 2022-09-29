class Solution:
    # Runtime: 283 ms, faster than 38.29% of Python3 online submissions for Longest Repeating Character Replacement.
    # Memory Usage: 13.8 MB, less than 93.23% of Python3 online submissions for Longest Repeating Character Replacement.
    def characterReplacement(self, s: str, k: int) -> int:
        dict_count_letters = {}
        begin = 0
        max_letter = 0
        longest_substring = 0
        for end in range(len(s)):
            dict_count_letters[s[end]] = 1 + dict_count_letters.get(s[end], 0)
            max_letter = max(max_letter, dict_count_letters[s[end]])
            if (end - begin + 1 - max_letter) > k:
                dict_count_letters[s[begin]] -= 1
                begin += 1
            longest_substring = max(longest_substring, end - begin + 1)
        return longest_substring