class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False

        table = defaultdict(int)

        for n in nums:
            table[n] += 1
        
        return max(table.values()) > 1