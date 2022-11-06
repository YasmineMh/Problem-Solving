class Solution:
    def countSubstrings(self, s: str) -> int:
        
        number_palindromic_substrings = 0
        
        for i in range(len(s)):
            
            left_odd, right_odd = i, i
            while left_odd >= 0 and right_odd < len(s) and s[left_odd]==s[right_odd]:
                number_palindromic_substrings += 1
                left_odd -= 1
                right_odd += 1
                
            left_even, right_even = i, i+1
            while left_even >= 0 and right_even < len(s) and s[left_even]==s[right_even]:
                number_palindromic_substrings += 1
                left_even -= 1
                right_even += 1
                
        return number_palindromic_substrings