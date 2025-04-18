from typing import List
class Sorting:
  def bubbleshort(array:List[int]):
    isswap=False
    for i in range(0,len(array)-1):
      for j in range(0,len(array)-i-1):
        if array[j]>array[j+1]:
          array[j+1],array[j]=array[j],array[j+1]
          isswap=True
    return array

  def selectionssort(array:List[int])-> List[int]:
    n=len(array)
    for i in range(0,n):
      small_element:int=i
      for j in range(i+1,n):
        if array[j]<array[small_element]:
          small_element=j
      array[i],array[small_element]=array[small_element],array[i]
    return array

  def insertionsort(array:List[int])->List[int]:
    for i in range(1,len(array)):
      current=array[i]
      previous=i-1
      while previous>=0 and array[previous]>current:
        array[previous+1]=array[previous]
        previous-=1
        array[previous+1]=current

    return array












text=Sorting.bubbleshort([1,2,3,4,5])
text2=Sorting.selectionssort([3,4,5,1,3,5,6,7,9])
text3=Sorting.insertionsort([3,4,5,1,3,5,6,7,9])

print(text)
print(text2)
print(text3)