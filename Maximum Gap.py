class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        
        n = len(nums)
        min_val = min(nums)
        max_val = max(nums)
        
        if min_val == max_val:
            return 0
        
        # Minimum possible maximum gap (bucket size)
        bucket_size = max(1, (max_val - min_val) // (n - 1))
        bucket_count = (max_val - min_val) // bucket_size + 1
        
        buckets = [[None, None] for _ in range(bucket_count)]
        
        # Distribute numbers into buckets
        for num in nums:
            idx = (num - min_val) // bucket_size
            bucket = buckets[idx]
            
            if bucket[0] is None:
                bucket[0] = bucket[1] = num
            else:
                bucket[0] = min(bucket[0], num)
                bucket[1] = max(bucket[1], num)
        
        max_gap = 0
        prev_max = min_val
        
        # Calculate maximum gap
        for bucket in buckets:
            if bucket[0] is None:
                continue
            max_gap = max(max_gap, bucket[0] - prev_max)
            prev_max = bucket[1]
        
        return max_gap
