import math
from typing import List
class Solution(object):
    def maxSubArray(self,numbers:List[int])-> int:
        currentsum,maxsum = 0,-math.inf
        
        for start in range(len(numbers)):
            currentsum+=numbers[start]
            maxsum=max(currentsum,maxsum)
            if currentsum<0:
                currentsum=0
        return maxsum



solve=Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])

print(solve)

