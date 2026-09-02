class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        tally = []
        for idx, num in enumerate(nums):
            if num in tally: 
                return True
            else:
                tally.append(num)
        return False
        