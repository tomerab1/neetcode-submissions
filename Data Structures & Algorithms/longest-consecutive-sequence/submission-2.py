class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        s = set()

        for n in nums:
            s.add(n)
        
        max_count = 0
        for item in s:
            if (item-1) not in s:
                candidate = item
                count = 1
                while candidate + 1 in s:
                    count += 1
                    candidate += 1
                if count > max_count:
                    max_count = count

        return max_count