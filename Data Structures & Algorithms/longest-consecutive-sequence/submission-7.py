class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        size = 0
        for num in numset:
            cursize = 0
            while num+cursize in numset:
                cursize+=1
            size= max(size,cursize)
        return size