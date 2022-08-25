class Solution:
    
    #Runtime: 1347 ms, faster than 50.57% of Python3 online submissions for 3Sum.
    #Memory Usage: 19 MB, less than 8.70% of Python3 online submissions for 3Sum.
    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        tuplesSet = set()
        resultList = []
        nums.sort()
        
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            
            begin, end = i+1, len(nums)-1
            
            while begin<end:
                
                sumNumbers = nums[i] + nums[begin] + nums[end]
                
                if sumNumbers > 0:
                    end -= 1
                    
                elif sumNumbers < 0:
                    begin += 1
                    
                else:
                    if (nums[i], nums[begin], nums[end]) not in tuplesSet:
                        resultList.append([nums[i], nums[begin], nums[end]])
                        tuplesSet.add((nums[i], nums[begin], nums[end]))
                    end -= 1
                    begin += 1
        return resultList        
    

    
    #Runtime: 735 ms, faster than 93.37% of Python3 online submissions for 3Sum.
    #Memory Usage: 18.1 MB, less than 40.35% of Python3 online submissions for 3Sum.
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        resultList = []
        nums.sort()
        
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            
            begin, end = i+1, len(nums)-1
            
            while begin<end:
                
                sumNumbers = nums[i] + nums[begin] + nums[end]
                
                if sumNumbers > 0:
                    end -= 1
                    
                elif sumNumbers < 0:
                    begin += 1
                    
                else:
                    resultList.append([nums[i], nums[begin], nums[end]])
                    end -= 1
                    begin += 1
                    while nums[begin]==nums[begin-1] and begin<end:
                        begin += 1
                    while nums[end]==nums[end+1] and begin<end:
                        end -= 1
                    
        return resultList  