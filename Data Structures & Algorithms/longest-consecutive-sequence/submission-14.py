class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0
        for num in numset:
            curcount = 1
            if num - 1 not in numset:
                curcount = 1
                while num + curcount in numset:
                    curcount+=1
            longest = max(curcount,longest)
        return longest