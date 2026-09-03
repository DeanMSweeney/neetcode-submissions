class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        cp = list(nums)
        for idx, n in enumerate(nums):
            cp.append(n)
        return cp
