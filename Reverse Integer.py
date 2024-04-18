class Solution:
    def reverse(self, x: int) -> int:
      while True:
        if x<0:
          x = int(str(x)[1:][::-1]) * -1
        else:
          x = int(str(x)[::-1])
        if x < -2**31 or x > 2**31-1:
          return 0
        return x
      

