from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
     start=0;end=len(nums)-1
     n=len(nums)
     if (n==1):
        return nums[0]
     while(start<=end):
        mid=start+(end-start)//2
        
        if (mid > 0 and nums[mid - 1] != nums[mid]) and (mid < n - 1 and nums[mid + 1] != nums[mid]):
                return nums[mid]
        if (mid%2)==0:
            if nums[mid-1]!=nums[mid]:
                start=mid+1
                
            else:
                end=mid-1
        else:
            if nums[mid-1]!=nums[mid]:
                end=mid-1
            else:
                start=mid+1




x=Solution().singleNonDuplicate([3,3,7,7,10,11,11])
print(x)