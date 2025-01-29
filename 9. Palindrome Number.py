class Solution(object):
    def isPalindrome(self, x: int) -> bool:
        invertnumber:int =0
        y=x
        while x>0:
            last=x%10
            invertnumber=(invertnumber*10)+last
            x=x//10
        return invertnumber==y







# Aooroch 2


class Solutions(object):
       def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False

        if x!=0 and x%10==0:
            return False
        half_number=