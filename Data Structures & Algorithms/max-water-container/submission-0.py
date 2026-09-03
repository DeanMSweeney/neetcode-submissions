class Solution:
    def maxArea(self, heights: List[int]) -> int:
        h = heights
        l, r = 0, len(heights) - 1
        A = 0 
        while l < r: # two pointer 
            area = (r - l) * min(h[l], h[r]) # compute area
            if area > A: # update amax area 
                A = area
            #update l or b based on lower height 
            if h[l] < h[r]: 
                l += 1
            elif h[l] > h[r]:
                r -= 1
            else: 
                l += 1
        return A