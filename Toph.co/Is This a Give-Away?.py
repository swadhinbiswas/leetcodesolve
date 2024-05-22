brackests=input()
print(brackests)

for i in brackests:
  if i=='}':
    brackests.pop(i)
    
print(brackests)