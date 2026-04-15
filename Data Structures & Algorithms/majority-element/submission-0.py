class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res_map = defaultdict(int)
        res = maxCount = 0
        for ele in nums :
            res_map[ele] += 1
            if maxCount < res_map[ele]:
                res = ele 
                maxCount = res_map[ele]
        
        return res

        



      