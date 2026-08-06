class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = Counter(nums)
        l = 0
        for i in range(3):

            for write in range(l,l+count[i]):
                nums[write] = i
            l+=count[i]    