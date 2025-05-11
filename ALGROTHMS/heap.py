class Heap:
   def __init__(self):
    self.heap=[]

  def _parent(self,i):
    return (i-1)//2
  def _left_child(self,i):
    return 2*i+1
  def _right_child(self,i):
    return 2*i+2
  def _swap(self,i,j):
    self.heap[i],self.heap[j]=self.heap[j],self.heap[i]
  def insert(self,value):
    self.heap.append(value)
    self._heapify_up(len(self.heap)-1)
  def _heapify_up(self,i):
    while i>0 and self.heap[i]<self.heap[self._parent(i)]:
      self._swap(i,self._parent(i))
      i=self._parent(i)
  def extract_min(self):
    if not self.heap:
      return None
    if len(self.heap)==1:
    return self.heap.pop()

    min_val=self.heap[0]
    self._heapify_down(0)
    return min_val
  def _heapify_down(self,i):
    min_index=1
    left=self._left_child(i)
    right=self._right_child(i)
    if left<len(self.heap) and self.heap[left]<self.heap[min_index]:
      min_index=right
    if i != min_index:
      self._swap(i,min_index)
      self._heapify_down(min_index)
  def peek_min(self):
    if self.heap:
      return self.heap[0]
    return None
  def is_empty(self):
    return len(self.heap)==0

  def size(self):
    return len(self.heap)




class MaxHeap:
  def __init__(self):
    self.heap=[]

  def _parent(self,i):
    return (i-1)//2
  def _left_child(self,i):
    return 2*i+1

  def _right_child(self,i):
    return 2*i+2
  def _swap(self,i,j):
    self.heap[i],self.heap[j]=self.heap[j],self.heap[i]
  def insert(self,value):
    self.heap.append(value)
    self._heapify_up(len(self.heap)-1)
  def _heapify_up(self,i):
    while i>0 and self.heap[i]>self.heap[self._parent[i]]:
      self._swap(i,self._parent(i))
      i=self._parent(i)
  def delete(self,value):
    self._heapify_down(self.i)
  def _heapify_down(self,i):
    max_index=i
    left=self._left_child(i)
    right=self._right_child(i)
    if left<len(self.heap) and self.heap[left] >self.heap[max_index]:
      max_index=left
    if right<len(self.heap) and self.heap[right]>self.heap[max_index]:
      max_index=right

    if i!=max_index:
      self._swap(i,max_index)
      self._heapify_down(max_index)

  def peek_max(self):
    if self.heap:
      return self.heap[0]

  def is_empty(self):
    return len(self.heap)==0
  def size(self):
    return len(self.heap)

