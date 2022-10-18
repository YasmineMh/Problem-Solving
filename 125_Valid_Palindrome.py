class Solution:
    
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