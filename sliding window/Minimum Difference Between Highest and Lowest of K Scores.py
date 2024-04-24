class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return 0
        nums.sort()
        d = float('inf')
        for i in range(len(nums) - k + 1):
            diff = abs(nums[i] - nums[i+k-1])
            d = min(diff,d)
        return d