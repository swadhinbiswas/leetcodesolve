

class Solution(object):
    def maxSubarray(self,array):
        max_sum = -1
        for start in range(len(array)):
            arraysum=0
            for end in range(start,len(array)):
                arraysum+=array[end]
                max_sum=max(max_sum,arraysum)

        return max_sum




x=Solution().maxSubarray([3,-4,5,4,-1,12,-8])
print(x)
            
