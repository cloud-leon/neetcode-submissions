class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        summap = {}
        for index, number in enumerate(nums):
            diff = target - number
            if diff not in summap:
                summap[number] = index
            else:
                return [summap[diff],index]