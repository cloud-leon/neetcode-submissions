class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums)+1)]
        count = {}
        res= []
        for num in nums:
            count[num] = count.get(num,0) +1

        for number,cnt in count.items():
            freq[cnt].append(number)
        for i in range(len(freq)-1,-1,-1):
            for num in freq[i]:
                if len(res) < k:
                    res.append(num)
            if len(res)== k:
                break
                
        return res