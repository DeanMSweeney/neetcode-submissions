class Solution:
    def search(self, nums: List[int], target: int) -> int:
        map = {} # build hash map of value: index pairs 
        for idx, n in enumerate(nums):
            map[n] = idx 
        
        return map.get(target, -1)
