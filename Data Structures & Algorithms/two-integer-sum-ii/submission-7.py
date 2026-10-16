class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r = 0, len(numbers)-1
        while l < r:
            size = numbers[l] + numbers[r]
            if size > target:
                r-=1
            elif size == target:
                return [l+1,r+1]
            else:
                l+=1
