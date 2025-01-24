import math

class Solution(object):
    def maxSubarray(self,array):
        max_sum = -math.inf
        for start in range(len(array)):
            arraysum=0
            for end in range(start,len(array)):
                arraysum+=array[end]
                max_sum=max(max_sum,arraysum)

        return max_sum


