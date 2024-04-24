class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        i = 0
        ans = 0
        p = 1
        for j in range(len(nums)):
            p = p*nums[j]
            while(p >= k):
                p = p//nums[i]
                i += 1
            ans += (j-i+1)
        return ans