class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = defaultdict(list)

        for s in strs:
            k = [0] * 27

            for c in s:
                k[ord(c) - ord('a')] += 1
            
            key = tuple(k)
            table[key].append(s)

        return [v for v in table.values()]
