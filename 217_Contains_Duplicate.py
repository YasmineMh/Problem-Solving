class Solution:
    def containsDuplicateDict(self, nums: List[int]) -> bool:
        # Runtime: 685 ms, faster than 50.09% of Python3 online submissions for Contains Duplicate.
        # Memory Usage: 26 MB, less than 71.55% of Python3 online submissions for Contains Duplicate.
        dict_nums = {}
        for i in nums:
            if i in dict_nums:
                return True
            dict_nums[i]=1
        return False
    
    def containsDuplicateSet(self, nums: List[int]) -> bool:
        #Runtime: 592 ms, faster than 68.23% of Python3 online submissions for Contains Duplicate.
        #Memory Usage: 25.9 MB, less than 71.55% of Python3 online submissions for Contains Duplicate.
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False