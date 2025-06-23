class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
      if indexDiff<0 or valueDiff<0:
        return False
      d={}
      bucket_lenth=indexDiff+1
      for i, num in enumerate(nums):
        bucket_index=num//bucket_lenth

        if bucket_index in d :
          return True
        if bucket_index-1 in d and abs(num-d[bucket_index-1])<=valueDiff:
          return True
        if bucket_index+1 in d and abs(num-d[bucket_index+1])<=valueDiff:
          return True

        d[bucket_index]=num
        if i>=indexDiff:
          oldindex=nums[i-indexDiff]//bucket_lenth
          if oldindex in d and d[oldindex]==nums[i-indexDiff]:
            del d[oldindex]

      return False