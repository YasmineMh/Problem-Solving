class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        longest_sub_s = ""
        
        for i in range(len(s)):
            
            left_odd, right_odd = i, i
            
            while left_odd >= 0 and right_odd < len(s) and s[left_odd]==s[right_odd]:
                if right_odd-left_odd+1 > len(longest_sub_s):
                    longest_sub_s = s[left_odd:right_odd+1]
                left_odd -= 1
                right_odd += 1
            
            left_even, right_even = i, i+1
            
            while left_even >= 0 and right_even < len(s) and s[left_even]==s[right_even]:
                if right_even-left_even+1 > len(longest_sub_s):
                    longest_sub_s = s[left_even:right_even+1]
                left_even -= 1
                right_even += 1
                
        return longest_sub_s