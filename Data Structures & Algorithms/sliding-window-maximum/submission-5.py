class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        heap = []
        for i in range(len(nums)-k+1):
            maxcur = nums[i]
            for j in range(i,i+k):
                maxcur=max(nums[j],maxcur)
            res.append(maxcur)
        return res