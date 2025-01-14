n,m=input().split()
n=int(n)
m=int(m)
array=[]
for i in range(n):
    arr2=list(map(str, input().split(",")))[:n]
    array.append(arr2)


for index,row in enumerate(array):
    stars=row[0].count('*')
    if stars==m:
        print(index+1)
        break



        


