class Solution:
    
    #Runtime: 155 ms, faster than 58.82% of Python3 online submissions for Top K Frequent Elements.
    #Memory Usage: 18.5 MB, less than 92.29% of Python3 online submissions for Top K Frequent Elements.
    def topKFrequent1(self, nums: List[int], k: int) -> List[int]:
        dict_stock = {}
        dict_values = {}
        for i in nums:
            if i not in dict_stock:
                dict_stock[i] = 0
            dict_stock[i] += 1
        
        for i in dict_stock:
            if dict_stock[i] not in dict_values:
                dict_values[dict_stock[i]] = []
            dict_values[dict_stock[i]].append(i)
        
        # print(dict_values)
        
        #the sort is O(n log n) both on average and in the worst case.
        keys_list = dict_values.keys()
        sorted_keys_list = sorted(keys_list, reverse=True)
        
        # print(sorted_keys_list)
        
        sorted_values = []
        
        for i in sorted_keys_list:
            sorted_values += dict_values[i]
        
        # print(sorted_values)
        
        return sorted_values[:k]
    
    #Runtime: 132 ms, faster than 75.18% of Python3 online submissions for Top K Frequent Elements.
    #Memory Usage: 19.7 MB, less than 15.19% of Python3 online submissions for Top K Frequent Elements.
    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        count = {}
        list_mapping = [[] for i in range(len(nums) + 1)]
        
        # print(list_mapping)
        
        for n in nums:
            count[n] = 1 + count.get(n, 0)
            
        # print(count)
        
        for n, c in count.items():
            list_mapping[c].append(n)
        
        # print(list_mapping)
        
        res = []
        for i in range(len(list_mapping) - 1, 0, -1):
            # print("i=",i)
            for n in list_mapping[i]:
                res.append(n)
                if len(res) == k:
                    return res
