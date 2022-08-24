class Solution:
    
    # ***************** Solution 1
    # Time Limit Exceeded
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
        
        return dict_s == dict_t

    
    def groupAnagrams1(self, strs: List[str]) -> List[List[str]]:
        dict_stock = {}
        
        for i in strs:
            done = False
            for j in dict_stock:
                if self.isAnagram(i, j):
                    dict_stock[j].append(i)
                    done = True
                    break
                    
            if not done:
                dict_stock[i] = []
        
        result_list = []
        
        for key in  dict_stock:
            anagram_list = [key]
            for value in dict_stock[key]:
                anagram_list.append(value)
            result_list.append(anagram_list)
            
        return result_list
    
    
    
    
    # ***************** Solution 2
    #Runtime: 306 ms, faster than 5.02% of Python3 online submissions for Group Anagrams.
    #Memory Usage: 18.6 MB, less than 37.09% of Python3 online submissions for Group Anagrams.
    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        dict_stock = {}

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord('a')] += 1
            
            if str(count) not in dict_stock:
                dict_stock[str(count)] = []
            dict_stock[str(count)].append(s)
        return dict_stock.values()
    

    
    
    # ***************** Solution 3
    #from typing import List
    #import collections
    #Runtime: 194 ms, faster than 27.55% of Python3 online submissions for Group Anagrams.
    #Memory Usage: 20 MB, less than 9.21% of Python3 online submissions for Group Anagram
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_stock = collections.defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord('a')] += 1
            
            dict_stock[tuple(count)].append(s)
            
        return dict_stock.values()