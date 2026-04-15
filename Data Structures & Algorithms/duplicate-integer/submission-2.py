class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freqMap = {}
        for index , ele in enumerate(nums):
            if ele in freqMap:
                return True 
            else:
                freqMap[ele] = index 
        
        return False 
        