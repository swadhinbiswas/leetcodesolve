# from typing import List

# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         productofall=1
#         for i in range(len(nums)):
#               productofall*=nums[i]
#         for i in range(len(nums)):
#             x=nums[i]
#             if x!=0:
#                 nums[i]=productofall//x
#         return nums
#         #Only For Positive Test Case


from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        array=[1]*n
        prefix=1
        for i in range(n):
            array[i]=prefix
            prefix*=nums[i]

        suffix:int=1 

        for i in range(n-2,-1,-1):
            suffix*=nums[i+1]
            array[i]*=suffix 

        return array





print(Solution().productExceptSelf([-1,1,0,-3,3]))


