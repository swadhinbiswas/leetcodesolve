# from typing import List

# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         i=len(nums)
#         if i==0:
#             return 0
#         else:
#           for j in range(len(nums)-1):
#             if nums[j] == nums[j+1]:
#                 nums[j] = '_'
#                 i=i-1
                



# nums = [1,1,2]
# solution = Solution()
# print(solution.removeDuplicates(nums)) # 2 [1,2,_]

from typing import List

class Solution:
   def removeDuplicates(self, nums: List[int]) -> int:
     nums[:] = sorted(set(nums))
     return len(nums)

      
          
nums = [1,1,2]

test="art"

