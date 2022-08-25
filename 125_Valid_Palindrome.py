class Solution:
    
    #Runtime: 101 ms, faster than 20.30% of Python3 online submissions for Valid Palindrome.
    #Memory Usage: 14.2 MB, less than 99.23% of Python3 online submissions for Valid Palindrome.
    def isPalindrome(self, s: str) -> bool:
        s_cleaned = ""
        for i in s:
            if i.isalnum():
                s_cleaned += i.lower()
        
        begin = 0
        end = len(s_cleaned)-1
        
        
        while begin<len(s_cleaned)/2 and end>=len(s_cleaned)/2:
            if s_cleaned[begin] != s_cleaned[end]:
                return False
            begin += 1
            end -= 1

        return True