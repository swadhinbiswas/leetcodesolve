inputnum=int(input())
listnum=list(map(int,input().strip().split()))[:inputnum]

print(max(listnum))