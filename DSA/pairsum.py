from typing import List

class Pair(object):
    def pairsum(self,numer:List[int],target:int)->List[int]:
        for i in range(len(number)):
            for j in range(i+1,number):
                if numbr[i]+number[j]==target:
                    return i,j


    def pairsumalternet(self,number:List[int],target:int)->List[int]:
        seen={}
        for i, num in enumerate(number):
            complement=target-num
            if complement in seen :
                return [seen[complement],i]
            seen[num]=i
        return []






x=Pair().pairsumalternet([1,2,3,4,5],9)
print(x)