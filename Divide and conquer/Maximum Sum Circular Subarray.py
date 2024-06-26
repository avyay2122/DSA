class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        def kadane(nums):
            max_cur = max_global = nums[0]
            for i in range(1,len(nums)):
                max_cur = max(nums[i], max_cur+nums[i])
                max_global = max(max_global,max_cur)
            return max_global

        max_linear = kadane(nums)
        total_sum = sum(nums)
        max_wrap = total_sum+kadane([-x for x in nums])

        return max(max_linear, max_wrap) if max_wrap!=0 else max_linear