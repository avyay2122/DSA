class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        s1 = set()
        ans = 0
        sum = 0
        i = 0
        for j in range(len(nums)):
            while nums[j] in s1:
                s1.remove(nums[i])
                sum -= nums[i]
                i += 1
            s1.add(nums[j])
            sum += nums[j]
            ans = max(ans,sum)
        return ans
