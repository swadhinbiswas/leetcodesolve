#Broutforce method
from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:

        if len(height)<=2:
           return height[0]*1


        else:
            res=0
            l,r=0,len(height)-1

            while l<r:
                area=(r-1)*min(height[l], height[r])
                res=max(res, area)
                
                if height[l]<height[r]:
                    l+=1
                else:
                    r-=1

            return res


height =[1,1]
soluction=Solution()
x=soluction.maxArea(height)
print(x)
