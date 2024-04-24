class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key = lambda x:(-x[0],x[1]))
        defe = 0
        weak = 0
        for a,d in properties:
            if d < defe:
                weak += 1
            else:
                defe = d
        return weak