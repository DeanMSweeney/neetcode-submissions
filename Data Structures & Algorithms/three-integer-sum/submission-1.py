class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # O(nlogn)
        out = []
        for idx, n in enumerate(nums):
            if n > 0: # if the first element is positive, break loop 
                break 
            
            if idx > 0 and n == nums[idx - 1]: # skip duplicates for the first number 
                continue 
            
            l = idx + 1 # assign left bound as next integer
            r = len(nums) - 1 # assign right bound as next integer
            while l < r: 
                ts = n + nums[l] + nums[r] # compute three sum 
                if ts > 0: 
                    r -= 1 # lower sum
                elif ts < 0: 
                    l += 1 # increase sum 
                else:
                    out.append([n, nums[l], nums[r]]) 
                    l += 1 
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r: # avoid duplicate l 
                        l += 1
        return out 

            
                       
