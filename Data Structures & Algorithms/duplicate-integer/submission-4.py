class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dups_set = set()
        for ele in nums:
            if ele not in dups_set:
                dups_set.add(ele)
            else:
                return True 

        return False 
       