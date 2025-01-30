class Solution:
   
    def myPow(self, x: float, n: int) -> float:
        def helper(x,n):
            if n==0:return 1
            if x==0:return 0
            res=helper(x*x,n//2)
            return x*res if n%2!=0 else res
        res=helper(x,abs(n))
        return res if n>=0 else 1/res

            

