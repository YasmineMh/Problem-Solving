class Solution:
    
    def fillDict(self, listToConvert: list) -> dict:
        dictFromList = collections.defaultdict(int)
        for i in listToConvert:
            dictFromList[i] += 1
        return dictFromList
    
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict_ransomNote = self.fillDict(ransomNote)
        dict_magazine = self.fillDict(magazine)
        
        for i in dict_ransomNote:
            if i not in dict_magazine or dict_ransomNote[i]>dict_magazine[i]:
                return False
            
        return True