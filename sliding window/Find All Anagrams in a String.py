from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        k = len(p)
        pvalues = Counter(p)
        l = []
        for i in range(len(s)-k+1):
            if Counter(s[i:i+k]) == pvalues:
                l.append(i)
        return l