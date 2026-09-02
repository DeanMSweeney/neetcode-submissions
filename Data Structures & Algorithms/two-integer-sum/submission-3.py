class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}

        for idx, n in enumerate(nums):
            hash[n] = idx 
        
        for idx, n in enumerate(nums): 
            diff = target - n 
            if diff in nums and hash[diff] != idx: 
                return [idx, hash[diff]]

                
            


        