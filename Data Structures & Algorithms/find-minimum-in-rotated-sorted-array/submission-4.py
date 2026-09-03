class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0 
        r = len(nums) - 1
        sol = nums[0]

        while l <= r: 
            if nums[l] < nums[r]:
                sol = min(sol, nums[l])
                break 
            m = (l + r) // 2
            sol = min(sol, nums[m])

            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return sol






        