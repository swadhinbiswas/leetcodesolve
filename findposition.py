class Solution:
    def searchInsert(self, nums, target: int) -> int:
      for i in range(0,len(nums)):
        if nums[i]==target:
          break
        return i
      