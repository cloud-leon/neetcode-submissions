class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        array = []

        def dfs(hold,i):
            if i == len(nums):
                array.append(hold.copy())
                return 
            hold.append(nums[i])
            dfs(hold,i+1)
            hold.pop()
            dfs(hold,i+1)

        dfs([],0)
        return array