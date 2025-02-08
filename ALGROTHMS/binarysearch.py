# def findesoluction(num1:int,num2:int):
#     while(num1 < num2):
#         mid=(num1+num2)//2
#         count=count+1
#         if (number2>mid):
#             number1=mid+1
#         else: number2=mid

#     return count


# num1,num2=input().split()

from typing import List

class SearchALgo:
    def binarysearch(array:List[int],target:int):
        start=0;end=len(array)-1
        while(start<=end):
            mid=(start+end)//2
            if (target>array[mid]):
                start=mid+1
            elif (target<array[mid]):
                end=mid-1
            else:
                return mid 
        return -1
    def optimizedBinarysearch(array:List[int],target:int):
        start=0;end=len(array)-1
        while(start<=end):
            mid=start+(end-start)//2
            if (target>array[mid]):
                start=mid+1
            elif (target<array[mid]):
                end=mid-1
            else:
                return mid
        return -1

    


array=[1,2,5,6,7,8,9]

x=SearchALgo.optimizedBinarysearch(array,6)
print(x)
