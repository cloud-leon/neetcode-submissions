class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        freq = [[] for i in range(len(nums)+1)]
        count = {}
        for num in nums:
            count[num] = count.get(num,0) + 1 
        for key, value in count.items():
            freq[value].append(key)
        
        for i in range(len(freq)-1,-1,-1):
            for item in freq[i]:
                if len(res) < k:
                    res.append(item)
            if len(res) ==k:
                break
        return res