class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zero_cnt = 0
        for n in nums:
            if n: 
                prod *= n
            else: 
                zero_cnt += 1
        if zero_cnt > 1: # if there are more than two zeros, soln will be zero 
            return [0] * len(nums)

        res = [0] * len(nums)
        for idx, c in enumerate(nums): 
            if zero_cnt: res[idx] = 0 if c else prod 
            else: res[idx] = prod // c
        return res  
            


