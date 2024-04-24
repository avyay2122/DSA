class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        count = 0
        s = str(num)
        for i in range(k,len(s) + 1):
            divi = int(s[i-k:i])
            if divi != 0 and num % divi == 0:
                count += 1
        return count