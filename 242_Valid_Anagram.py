class Solution:
    
    def fillDict(self, s: str) -> dict:
        dict_s = {}
        for i in s:
            if i not in dict_s:
                dict_s[i] = 0
            dict_s[i] += 1
        return dict_s
    
    

    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        dict_t = {}
        
        dict_s = self.fillDict(s)
        dict_t = self.fillDict(t)
        
        if dict_s == dict_t:
            return  True
        return False
        
