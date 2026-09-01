class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        table = defaultdict(int)

        for n in nums:
            table[n] += 1
        
        max_count = max(table.values())
        buckets = [[] for _ in range(max_count + 1)]

        for c, v in table.items():
            buckets[v].append(c)

        res = []
        for b in buckets[::-1]:
            if k > 0:
                res.extend(b)
                k -= len(b)


        return res


