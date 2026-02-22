class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max = nums[0]
        cur_min = nums[0]
        result = nums[0]
        
        for i in range(1, len(nums)):
            n = nums[i]
            
            # If number is negative, swap max and min
            if n < 0:
                cur_max, cur_min = cur_min, cur_max
            
            cur_max = max(n, cur_max * n)
            cur_min = min(n, cur_min * n)
            
            result = max(result, cur_max)
        
        return result
