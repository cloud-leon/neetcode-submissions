from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        count = Counter(nums)
        freq = [[] for i in range(len(nums)+1)]
        for num,counts in count.items():
            freq[counts].append(num)
        for i in range (len(freq)-1,-1,-1):
            for j in freq[i]:
                result.append(j)
                if len(result)==k:
                    return result
        