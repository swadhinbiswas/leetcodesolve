a=[int(i) for i in __import__('sys').stdin]
print(a[0]*(a[0]+1)//2-sum(a[2:]))