class Solution:
    def maximumSwap(self, num: int) -> int:
        num = [int(x) for x in str(num)]
        last_index = {val: i for i, val in enumerate(num)}
        for i in range(len(num)):
            for d in range(9, num[i], -1):
                if d in last_index and last_index[d] > i:
                    num[i], num[last_index[d]] = num[last_index[d]], num[i]
                    return int("".join(map(str, num)))
        return int("".join(map(str, num)))
