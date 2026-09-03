class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1 

        while l <= r: 
            if nums[l] == target: # check l, r values
                return l
            elif nums[r] == target:
                return r 

            m = (l + r) // 2 # compute midpt and check val
            if nums[m] == target:
                return m 

            if nums[m] > target: # update l, r 
                r = m -1 
            elif nums[m] < target: 
                l = m + 1 
        return -1 
            
        