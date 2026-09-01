class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = defaultdict(list)

        for s in strs:
            k = [0] * 26

            for c in s:
                k[ord(c) - ord('a')] += 1
            
            key = tuple(k)
            table[key].append(s)

        return list(table.values())
