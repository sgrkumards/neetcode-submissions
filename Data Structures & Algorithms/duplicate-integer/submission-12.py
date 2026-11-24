class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ans = set()
        for ele in nums :
            if ele in ans:
                return True 
            ans.add(ele)
        return False 

        