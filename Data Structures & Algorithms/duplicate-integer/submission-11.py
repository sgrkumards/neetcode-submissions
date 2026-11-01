class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set() # recording element in set as it holds only unique reocrd 

        for  num in nums:
            if num in seen:
                return True 
            seen.add(num)
        return False
   

# Flow chart or psrdo code 

# begin 


#     need to iterate through the nums 
#     record the ietareted array or seend element of array 
#     if find any repeating we wil imdetaialy return True 

#     after all the ierteof lelemne tin arrayt if we did not find anything we will 
#     retiurn False

# end 