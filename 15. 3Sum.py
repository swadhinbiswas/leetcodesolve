from collections import defaultdict

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        negative = defaultdict(int)
        positive = defaultdict(int)
        zeros = 0
        for num in nums:
            if num < 0:
                negative[num] += 1
            elif num > 0:
                positive[num] += 1
            else:
                zeros += 1

        result = []
        if zeros:
            for n in negative:
                if -n in positive:
                    result.append((0, n, -n))
            if zeros > 2:
                result.append((0,0,0))

        for set1, set2 in ((negative, positive), (positive, negative)):
            set1Items = list(set1.items())
            for i, (j, k) in enumerate(set1Items):
                for j2, k2 in set1Items[i:]:
                    if j != j2 or (j == j2 and k > 1):
                        if -j-j2 in set2:
                            result.append((j, j2, -j-j2))
        return result





class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
      answer=[]
      size=len(nums)-1
      nums=nums.sort()
      nums=list(set(nums))
      ans=[]
      for i in range(size):
        j=i+1;k=size
        while(j<k):
          add=nums[i]+nums[j]+nums[k]
          if add<0:
            j=j+1
          elif add>0:
            k=k+1
          else:
            ans.append([num[i],nums[j],nums[k]])

      return ans 
