class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            srtS = ''.join(sorted(s))
            res[srtS].append(s)

        return list(res.values())

        