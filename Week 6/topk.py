class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_freq = {}
        for num in nums:
            if num in dict_freq:
                dict_freq[num] += 1
            else:
                dict_freq[num] = 1
            
        sorted_dict = dict(sorted(dict_freq.items(), 
                          key=lambda item: item[1]))

        returnval = []
        for key in sorted_dict:
            returnval.append(key)
        # print(sorted_dict)
        return returnval[-k:]