class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grp_freq = defaultdict(list)
        for char in strs :
            grp_freq[tuple(sorted(char))].append(char)

         
        return list(grp_freq.values())
        