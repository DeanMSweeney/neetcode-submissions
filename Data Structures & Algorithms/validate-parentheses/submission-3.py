class Solution:
    def isValid(self, s: str) -> bool:

        # build dict of partners: 
        left = ['(', '{', '[']
        right = [')', '}', ']']
        map = {}

        for idx, e in enumerate(right):
            map[e] = left[idx]

        # iteratre through list 
        stack = []

        for idx, p in enumerate(s):
            if p in map:
                if stack and stack[-1] == map[p]:
                    stack.pop() #remove last element 
                else:
                    return False
            else:
                stack.append(p)
        
        return False if stack else True
        

        


