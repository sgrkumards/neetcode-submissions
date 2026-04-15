class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        h = set()
        for ele in nums:
            if ele in h :
                return True
            h.add(ele)
        return False
         