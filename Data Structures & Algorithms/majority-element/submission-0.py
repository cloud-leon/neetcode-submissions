class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {0:1}

        for num in nums:
            count[num] = 1 + count.get(num,0)
            if count[num] > len(nums) //2 :
                return num
        