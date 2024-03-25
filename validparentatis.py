class Solution:
    def isValid(self, s: str) -> bool:
      stack=[]
      openbracket={
        '[':1,'{':2,'(':3,
      }
      closebracket={
        ']':1,'}':2,')':3,
      }
      
      for i in s:
        if i not in closebracket:
          stack.append(i)
        else:
          if len(stack)>0:
            pop_brack=stack.pop()
            if closebracket[i]==openbracket[pop_brack]:
              continue
            else:
              return False
          else:
            return False
          
      if len(stack)==0:
        return True
      else:
        return False