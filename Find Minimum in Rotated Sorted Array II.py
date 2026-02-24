class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            if nums[mid] < nums[right]:
                # Minimum is in left half (including mid)
                right = mid
            elif nums[mid] > nums[right]:
                # Minimum is in right half (excluding mid)
                left = mid + 1
            else:
                # nums[mid] == nums[right]
                # Cannot decide the side, reduce search space
                right -= 1
                
        return nums[left]
