
def watermellon(weight):
    if weight<=100:
       if weight%2==0 and weight>2:
        print("YES")
       else:
        print("NO")
    else:
        return -1

if __name__ == "__main__":
    weight=int(input())
    watermellon(weight)





