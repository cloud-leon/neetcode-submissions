class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        ten = nums
        def backtrack(i):
            if i == len(nums):
                res.append(ten[:])
                return 
            

            for j in range(i, len(nums)):
                ten[i],ten[j] = ten[j],ten[i]
                backtrack(i+1)
                ten[i],ten[j] = ten[j],ten[i]        
        backtrack(0)
        return res