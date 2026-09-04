class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1 # init 2-pointers 

        while l <= r: 
            diff_lr = (numbers[r] + numbers[l]) - target # compute movement func. 

            if diff_lr == 0 and l != r: 
                return [l + 1, r + 1]
            
            """
            m = (l + r) // 2 # compute midpt

            if diff_lr > 0: 
                diff_m = (numbers[m] + numbers[l]) - target
                if diff_m == 0 and l != m: 
                    return [l + 1, m + 1]
            elif diff_lr < 0: 
                diff_m = (numbers[m] + numbers[r]) - target
                if diff_m == 0 and r != m:
                    return [m + 1, r + 1] 
            """

            if diff_lr < 0: 
                l += 1 
            elif diff_lr > 0:
                r -= 1





        