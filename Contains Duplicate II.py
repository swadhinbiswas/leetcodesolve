class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        numslen=len(nums)
        d=set()
        j=0
        for i in range(numslen):
          if i-j>k:
            d.remove(nums[j])
            j+=1
          if nums[i] in d:
            return True
          d.add(nums[i])
        return False


"""
Dry Run
when i=0 j=0
and if 0-0<k







"""

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(set(nums))==len(nums):
            return False
        if len(nums)<=k+1:
            return True
        d={}
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]]=abs(d[nums[i]]-i)
                if d[nums[i]]<=k:
                    return True
                else:
                    d[nums[i]]=i
            else:
                d[nums[i]]=i
        return False



class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
      if len(set(nums))==len(nums):
            return False
      if len(nums)<=k+1:
            return True

      for i in range(len(nums)):
        pass
