class Solve:
    def binarysearch():
        start=0;end=10**6
        while(start<=end):
            mid=start+(end-start)//2
            print(mid)
            x=str(input()).lower()
            if x=="bigger":
                start=mid+1
            elif x=="smaller":
                end=mid-1
            elif x=="bingo":
                break
            else:
                break



Solve.binarysearch()