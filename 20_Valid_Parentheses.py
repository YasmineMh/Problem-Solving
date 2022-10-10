class Solution:
    def isValid(self, s: str) -> bool:
        dictChars = {')': '(', '}': '{', ']': '['}
        stack = []
        
        for i in s:
            if i not in dictChars:
                stack.append(i)
            else:
                if stack:
                    last = stack.pop()
                else:
                    last = '0'
                if last != dictChars[i]:
                    return False
                
        return not stack
