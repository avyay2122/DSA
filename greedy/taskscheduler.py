class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dic = Counter(tasks)
        max_freq = max(dic.values())
        max_freq_task = sum(1 for count in dic.values() if count == max_freq)
        
        interval = (max_freq - 1) * (n+1) +(max_freq_task)
        return max(interval,len(tasks))
