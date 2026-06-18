class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        re, cnt = 0,0 
        for num in nums:
            cnt  = cnt +1 if num else 0
            re =max(re,cnt)
        return re