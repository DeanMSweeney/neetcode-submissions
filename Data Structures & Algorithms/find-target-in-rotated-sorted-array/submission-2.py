class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r: 
            diff_l = nums[l] - target
            diff_r = nums[r] - target 
            
            if diff_l == 0: # return of l is target
                return l 
            elif diff_r == 0: # return if r is target 
                return r 

            # compute midpoint
            mp = (l + r) // 2
            diff_mp = nums[mp] - target
            
            if diff_mp == 0: # return if mp is target
                return mp

            if nums[mp] > nums[l]: # check if ordered 
                if diff_mp > 0: # move to smaller value 
                    if diff_l < 0: 
                        r = mp - 1 # ordered side
                    else:
                        l = mp + 1 # unordered side
                elif diff_mp < 0: # move to larger value 
                    l = mp + 1
            else: # right side ordered
                if diff_mp > 0: # move to smaller value
                        r = mp - 1 
                elif diff_mp < 0: # move to larger value
                    if diff_r > 0: 
                        l = mp + 1 
                    else:
                        r = mp - 1
        return -1


                    

            
