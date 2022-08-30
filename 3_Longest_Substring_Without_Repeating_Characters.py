class Solution:
    
    #Runtime: 67 ms, faster than 91.06% of Python3 online submissions for Longest Substring Without Repeating Characters.
    #Memory Usage: 14 MB, less than 49.86% of Python3 online submissions for Longest Substring Without Repeating Characters.
    def lengthOfLongestSubstring(self, s: str) -> int:
        longestSubstring = 0
        
        begin = 0
        stringSet = set()
        
        for end in range(len(s)):
            
            while s[end] in stringSet:
                stringSet.remove(s[begin])
                begin += 1
                
            stringSet.add(s[end])
            longestSubstring = max(longestSubstring, end - begin +1)
            
        
        return longestSubstring