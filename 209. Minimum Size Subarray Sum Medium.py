class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
       right,sumof,index=0,0,float('inf')
       for left in range(len(nums)):
        sumof+=nums[left]
        while sumof>=target:
          index=min(index,left-right+1)
          s-=nums[right]
          right+=1
       return 0 if index==float('inf') else index
