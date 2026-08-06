class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l, r = 0, len(height)-1 
        leftmax,rightmax = height[l], height[r]
        totalArea = 0

        while l < r:
            
            if leftmax < rightmax:
                l+=1
                leftmax = max(height[l],leftmax)
                totalArea += leftmax - height[l]
            else:
                r-=1
                rightmax = max(height[r],rightmax)
                totalArea += rightmax- height[r]
        return  totalArea