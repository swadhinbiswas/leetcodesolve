from typing import List

class Soluction:
  def isPossibe(array:List[int],maxAllowed,cowsNumber)->bool:
    cows=1;lastPositions=array[0]
    for i in len(array):
      if array[i]-lastPositions>=maxAllowed:
        cows+=1
        lastPositions=array[i]
      if cows==cowsNumber:
        return True

