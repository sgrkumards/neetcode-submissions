class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        has_map = set()
        for ele in nums :
            if ele not in has_map:
                has_map.add(ele)
            else:
                return True
        
        return False
