class Solution:
    def trap(self, height: List[int]) -> int:
        area = 0
        l,r = 0, len(height)-1
        leftmax,rightmax = height[l],height[r]
        while l < r:
            if leftmax <= rightmax:
                l+=1
                leftmax = max(height[l],leftmax)
                area += leftmax - height[l]
                
            else:
                r-=1
                rightmax = max(height[r],rightmax)
                area+= rightmax - height[r]
                

        return area