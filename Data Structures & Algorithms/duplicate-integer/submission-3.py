class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freqMap = {}
        for index , ele in enumerate(nums):
            if ele in freqMap:
                return True 
            
            freqMap[ele] = index 
        
        return False 
        