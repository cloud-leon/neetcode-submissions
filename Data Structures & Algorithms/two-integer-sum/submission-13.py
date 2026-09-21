class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hold = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in hold:
                return [hold[diff],i]
            hold[n] = i
        