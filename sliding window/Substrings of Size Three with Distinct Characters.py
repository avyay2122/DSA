class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        for i in range(3,len(s) + 1):
            k = s[i-3:i]
            g = set(k)
            if(len(g) == len(k)):
                count += 1
        return count