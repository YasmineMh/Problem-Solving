class Solution:
    
    #Runtime: 210 ms, faster than 47.35% of Python3 online submissions for Two Sum II - Input Array Is Sorted.
    #Memory Usage: 15.8 MB, less than 6.68% of Python3 online submissions for Two Sum II - Input Array Is Sorted.
    def twoSum1(self, numbers: List[int], target: int) -> List[int]:
        numbersDict = collections.defaultdict(list)
        for i in range(len(numbers)):
            numbersDict[numbers[i]].append(i+1)
            
        for i in numbers:
            diff = target - i
            if diff == i and len(numbersDict[i])>1:
                return numbersDict[i][:2]
                
            if diff in numbersDict:
                return [numbersDict[i][0],numbersDict[diff][0]]


    #Runtime: 259 ms, faster than 18.44% of Python3 online submissions for Two Sum II - Input Array Is Sorted.
    #Memory Usage: 14.9 MB, less than 89.77% of Python3 online submissions for Two Sum II - Input Array Is Sorted.
    def twoSum2(self, numbers: List[int], target: int) -> List[int]:
        begin, end = 0, len(numbers) - 1

        while begin < end:
            sum_begin_end = numbers[l] + numbers[r]

            if sum_begin_end > target:
                end -= 1
            elif sum_begin_end < target:
                begin += 1
            else:
                return [begin + 1, end + 1]