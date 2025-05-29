from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow=nums[0];fast=nums[0]
        while True:
          slow=nums[slow];fast=nums[nums[fast]]
          if slow==fast:
            break
        slow=nums[0]
        while(slow!=fast):
          slow=nums[slow]
          fast=nums[fast]
        return slow



# nums=[1,2,3,3,4]

# a = [0] * len(nums)
# for i in nums:
#             if a[i]:
#                 print(i)
#             a[i] = 1
