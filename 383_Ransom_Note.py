class Solution:
    
    def fillDict(self, listToConvert: list) -> dict:
        dictFromList = collections.defaultdict(int)
        for i in listToConvert:
            dictFromList[i] += 1
        return dictFromList
    
    #Runtime: 73 ms, faster than 73.69% of Python3 online submissions for Ransom Note.
    #Memory Usage: 14.1 MB, less than 94.49% of Python3 online submissions for Ransom Note.
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict_ransomNote = self.fillDict(ransomNote)
        dict_magazine = self.fillDict(magazine)
        
        for i in dict_ransomNote:
            if i not in dict_magazine or dict_ransomNote[i]>dict_magazine[i]:
                return False
            
        return True