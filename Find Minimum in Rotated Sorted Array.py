class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            # If mid element is greater than right, the min must be to the right
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                # Otherwise min is in left part (including mid)
                right = mid
        
        return nums[left]
