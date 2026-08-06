class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sumMap = {}
       

        for i, num in enumerate(nums):
            if target - num  not in sumMap:
                sumMap[num] = i
            else:
                return [sumMap[target-num],i]
        return []