class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)): 
            max_n = 0 
            for j in range(i + 1, len(arr)): 
                max_n = max(max_n, arr[j])

            arr[i] = max_n if i < len(arr) - 1 else -1
        return arr 

            

            

        