class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        map = {} # build hash map of element: count 
        for idx, n in enumerate(nums):
            map[n] = map.get(n, 0) + 1

        for k, v in map.items():
            if v > len(nums) / 2:
                return k


        