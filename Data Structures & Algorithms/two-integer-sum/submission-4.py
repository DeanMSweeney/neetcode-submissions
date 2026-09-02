class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        meta = {}

        for idx, n in enumerate(nums):
           meta[n] = idx 
        
        for idx, n in enumerate(nums): 
            diff = target - n 
            if diff in nums and meta[diff] != idx: 
                return [idx, meta[diff]]

                
            


        