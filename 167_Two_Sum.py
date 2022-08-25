class Solution:
    
    #Runtime: 210 ms, faster than 47.35% of Python3 online submissions for Two Sum II - Input Array Is Sorted.
    #Memory Usage: 15.8 MB, less than 6.68% of Python3 online submissions for Two Sum II - Input Array Is Sorted.
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numbersDict = collections.defaultdict(list)
        for i in range(len(numbers)):
            numbersDict[numbers[i]].append(i+1)
            
        for i in numbers:
            diff = target - i
            if diff == i and len(numbersDict[i])>1:
                return numbersDict[i][:2]
                
            if diff in numbersDict:
                return [numbersDict[i][0],numbersDict[diff][0]]