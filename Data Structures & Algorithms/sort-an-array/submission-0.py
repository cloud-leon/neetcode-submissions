class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
                
        arr = nums        
        n = len(nums)

        for i in range(n-1):
            min_idx= i
            for j in range(i + 1, n):
                if arr[j] < arr[min_idx]:
                
                    # Update min_idx if a smaller element is found
                    min_idx = j
                
            # Move minimum element to its
            # correct position
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return nums

