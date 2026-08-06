class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        targetlist = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in targetlist:
                return [targetlist[diff],i]
            targetlist[num] = i
