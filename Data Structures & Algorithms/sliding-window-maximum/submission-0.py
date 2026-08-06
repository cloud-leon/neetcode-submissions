class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        for i in range(len(nums) -k+1 ):
            curmax = nums[i]
            for j in range(i,k+i):
                curmax = max(curmax, nums[j])
            res.append(curmax)
        return res