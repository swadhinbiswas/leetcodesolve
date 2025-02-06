
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        leftpointer=0
        rightpointer=len(height)-1
        maxarea=0
        while leftpointer<rightpointer:
            h=min(height[leftpointer],height[rightpointer])
            width=rightpointer-leftpointer
            area=width*h
            maxarea=max(area,maxarea)
            if height[leftpointer]<height[rightpointer]:
                leftpointer+=1
            else:
                rightpointer-=1

        return  maxarea 


print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))



class Solution:
    def maxArea(self, height: List[int]) -> int:
        left,maxarea,right=0,0,len(height)-1
        while left<right:
                h=min(height[left],height[right])
                width=right-left
                area=h*width
                maxarea=max(area,maxarea)
                if height[left]<height[right]:
                    left+=1
                else:
                    right-=1
        return maxarea


print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))








