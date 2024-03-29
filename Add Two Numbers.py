# # class NodeList:
# #     def __init__(self, data=0, next=None):
# #         self.data = data
# #         self.next = next

# # class Solution:
# #    def addTwoNumbers(self,l1,l2):
# #         dummy = NodeList(0)
# #         current = dummy
# #         carry = 0
# #         while l1 or l2:
# #             x = l1.data if l1 else 0
# #             y = l2.data if l2 else 0
# #             sum = carry + x + y
# #             carry = sum // 10
# #             current.next = NodeList(sum % 10)
# #             current = current.next
# #             if l1:
# #                 l1 = l1.next
# #             if l2:
# #                 l2 = l2.next
# #         if carry > 0:
# #             current.next = NodeList(1)
# #         return dummy.next
      
      
# #  until both linked lists are exhausted, and if there is a remaining carry, a new node is added to the result.


# # solve=Solution()

# # l1 = NodeList(2)
# # l1.next = NodeList(4)
# # l1.next.next = NodeList(3)

# # l2 = NodeList(5)
# # l2.next = NodeList(6)
# # l2.next.next = NodeList(4)

# # result = solve.addTwoNumbers(l1, l2)

# # while result:
# #     print(result.data, end=" ")
# #     result = result.next




# #best case

# from typing import Optional

# class NodeList:
#     def __init__(self, data=0, next=None):
#         self.data = data
#         self.next = next

# class Solution:
#   def addTwoNumbers(self,l1:Optional[NodeList],l2:Optional[NodeList])->Optional[NodeList]:
#     outnode = NodeList(0)
    
#     current = outnode
#     carry = 0
#     while l1 or l2:
#       x=l1.data
#       y=l2.data
#       sum = carry + x + y
#       carry
# solve=Solution()

# l1 = NodeList(2)
# l1.next = NodeList(4)
# l1.next.next = NodeList(3)

# l2 = NodeList(5)
# l2.next = NodeList(6)
# l2.next.next = NodeList(4)

# result = solve.addTwoNumbers(l1, l2)

# while result:
#     print(result.data, end=" ")
#     result = result.next
  
  
#solve using list

# class Solution:
#     def addTwoNumbers(self, l1,l2):
      
      
# lsi=[2,4,3]
# lsi2=[5,6,4]
# out=[]
# carry=0

# for i in range(len(lsi)):
#   x=lsi[i]
#   y=lsi2[i]
#   sum=carry+x+y
#   carry=sum//10
#   out.append(sum%10)
# print(out)
from typing import Optional

class NodeList:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

class Solution:
    def addTwoNumbers(self, l1:Optional[NodeList],l2:Optional[NodeList])->Optional[NodeList]:
      outnode = NodeList(0)
      tail=outnode
      carry=0
      while l1 or l2:
        x=l1.val if l1 else 0
        y=l2.val if l2 else 0
        sum=carry+x+y
        carry=sum//10
        tail.next=NodeList(sum%10)
        tail=tail.next
        if l1:
          l1=l1.next
        if l2:
          l2=l2.next
      if carry>0:
        tail.next=NodeList(1)
      return outnode.next
    
      
solve=Solution()
lsi=[0]
lsi2=[0]
print(solve.addTwoNumbers(lsi,lsi2))
