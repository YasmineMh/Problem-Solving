class Solution:
    # Runtime: 199 ms, faster than 39.61% of Python3 online submissions for Permutation in String.
    # Memory Usage: 14 MB, less than 68.09% of Python3 online submissions for Permutation in String.
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1)>len(s2):
            return False
        
        hashMapS1 = [0] * 26
        hashMapS2 = [0] * 26
        
        checkMatches = 0
        
        for i in range(len(s1)):
            hashMapS1[ord(s1[i])-ord('a')] += 1 
            hashMapS2[ord(s2[i])-ord('a')] += 1
        
        for i in range(26):
            checkMatches += 1 if hashMapS1[i]==hashMapS2[i] else 0
        
        previous = 0
        for i in range(len(s1),len(s2)):

            if checkMatches == 26:
                return True
            
            indexNext = ord(s2[i]) - ord('a')
            boolBeforeNext = hashMapS2[indexNext]==hashMapS1[indexNext]
            
            hashMapS2[indexNext] += 1
            if hashMapS2[indexNext]==hashMapS1[indexNext]:
                checkMatches += 1
            elif not boolBeforeNext:
                pass
            else:
                checkMatches -= 1
            
            indexPrevious = ord(s2[previous]) - ord('a')
            boolBeforePrevious =  hashMapS2[indexPrevious] == hashMapS1[indexPrevious]
            
            hashMapS2[indexPrevious] -= 1
            previous += 1
            if hashMapS2[indexPrevious] == hashMapS1[indexPrevious]:
                checkMatches += 1
            elif not boolBeforePrevious:
                pass
            else:
                checkMatches -= 1
        

        return checkMatches == 26